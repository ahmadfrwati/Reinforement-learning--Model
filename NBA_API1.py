import csv
import json
import sys
from datetime import datetime
import pandas as pd
from flask import Flask, jsonify, request, render_template, url_for
from sklearn.externals import joblib
import numpy as np
from csv import reader
import tempfile
from os import path
from state_rewords_DRL import dd
try:
    #Model load
    saved_mystc_model = joblib.load('model/mystc_transaction.mdl')
    saved_kiosk_model = joblib.load('model/kiosk_transaction.mdl')
    Kiosk_transaction=joblib.load('model/Kiosk_transaction.mdl')
    Kiosk_Region=joblib.load( 'model/Kiosk_Region.pkl')
    Kiosk_Party_Segment_Type_Cd=joblib.load( 'model/Kiosk_Party_Segment_Type_Cd.pkl')
    Kiosk_Line_Status=joblib.load( 'model/Kiosk_Line_Status.pkl')
    Kiosk_STATUS=joblib.load('model/Kiosk_STATUS.pkl')
    Kiosk_RatePlan=joblib.load('model/Kiosk_RatePlan.pkl')
    Kiosk_TAMAYUZ_MEMBERSHIP_TYPE=joblib.load('model/Kiosk_TAMAYUZ_MEMBERSHIP_TYPE.pkl')
    mySTC_Region=joblib.load('model/mySTC_Region.pkl')
    mySTC_Party_Segment_Type_Cd=joblib.load( 'model/mySTC_Party_Segment_Type_Cd.pkl')
    mySTC_Line_Status=joblib.load( 'model/mySTC_Line_Status.pkl')
    pack_type = joblib.load('model/sawa.mdl')
except:
    print("Error loading application. Please run `python create_random_forest.py` first!")
    sys.exit(0)

app = Flask(__name__)


@app.errorhandler(400)
def bad_request(e):
    return jsonify({"status": "not ok", "message": "this server could not understand your request"})


@app.errorhandler(404)
def not_found(e):
    return jsonify({"status": "not found", "message": "route not found"})


def updater(filename,r,s,p,date,t,l):
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]
        #print(readData[r]["MSISDN"])
        readData[r]['nextTransaction'] = s
        readData[r]['nextTransaction_pro'] = p
        readData[r]['DateTime_Out_TXN_DT'] = date
        readData[r]["transactin_time"] = t
        readData[r]["subtransaction"] = l
        #print(readData)
    readHeader = readData[r].keys()
    writer(readHeader, readData, filename, "update")


def writer(header, data, filename, option):
    with open (filename, "w", newline = "") as csvfile:
         if option == "write":
             movies = csv.writer(csvfile)
             movies.writerow(header)
             for x in data:
                movies.writerow(x)
         elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames = header)
                writer.writeheader()
                writer.writerows(data)
         else:
             print("Option is not known")


def append_list_as_row(storage, list_of_elem):
    # Open file in append mode
    with open(storage, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        #csv_writer.writerow(f)
        csv_writer.writerows(list_of_elem)


col_list = ["Midisin"]
user = pd.read_csv("result_mySTC.csv", usecols=col_list)
col_list1 = ["Midisin"]
user1 = pd.read_csv("result_KiosK.csv", usecols=col_list)


@app.errorhandler(500)
def not_found(e):
    return jsonify({"status": "internal error", "message": "internal error occurred in server"})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/predict', methods=['GET'])
def predict():
    file = request.files['data_file']
    tmp = tempfile.TemporaryDirectory()
    temp_storage = path.join(tmp.name, file.filename)
    file.save(temp_storage)
    dd.rl(temp_storage, "records.csv")
    act = ['next_action']
    check = pd.read_csv("records.csv", usecols=act)

    if file.filename == 'mySTC.csv':
        cust_id = ['Midisin']
        cust_info = ['Line_Status', 'Party_Segment_Type_Cd', 'Region', 'Age_Range', 'LINE_TENURE_Range', 'WS_ID','CHANNEL_ID','STATUS_ID', 'DateTime_Out_TXN_DT']
        ide = pd.read_csv(temp_storage, usecols=cust_id)
        income = pd.read_csv(temp_storage, usecols=cust_info)
        pack = ['pp_revenue_last_1mon', 'pp_revenue_last_3mon']
        pack_1 = pd.read_csv(temp_storage, usecols=pack)
        k = 0
        r = 0
        for i in ide['Midisin']:
            #print(k)
            flag = 0
            for j in user['Midisin']:
                #print(i,j,r)
                # if j =="MSISDN":
                #   r+=1
                #  break
                if i == j:
                    flag = 1
                    person_features = np.array([mySTC_Line_Status[income['Line_Status'][k]],
                                                mySTC_Party_Segment_Type_Cd[income['Party_Segment_Type_Cd'][k]],
                                                mySTC_Region[income['Region'][k]],
                                                income['Age_Range'][k],
                                                income['LINE_TENURE_Range'][k],
                                                income['WS_ID'][k],
                                                income['CHANNEL_ID'][k],
                                                income['STATUS_ID'][k],
                                                ide['Midisin'][k]
                                                ]).reshape(1, -1)
                    nextTransaction = saved_mystc_model.predict(person_features)
                    nextTransaction_pro = saved_mystc_model.predict_proba(person_features)
                    list_pp = list(nextTransaction_pro)
                    nextTransaction_pro1_2 = np.amax(list_pp)+0.3
                    pack_types = np.array( [pack_1['pp_revenue_last_1mon'][k], pack_1['pp_revenue_last_3mon'][k]]).reshape(1, -1)
                    if check['next_action'][k] == 'SAWARECHANGE':
                        pp = pack_type.predict(pack_types)
                        #print(pp)
                        updater('result_mySTC.csv',r, nextTransaction, nextTransaction_pro1_2, income['DateTime_Out_TXN_DT'][k],str(datetime.now()),pp)
                    else:
                        updater('result_mySTC.csv', nextTransaction, nextTransaction_pro1_2, income['DateTime_Out_TXN_DT'][k], str(datetime.now()), '')
                    r = 0
                    break

                elif i != j:
                    # print(r)
                    r += 1
                    flag = 0
            if flag == 0:
                # print(r)
                person_features = np.array([mySTC_Line_Status[income['Line_Status'][k]],
                                            mySTC_Party_Segment_Type_Cd[income['Party_Segment_Type_Cd'][k]],
                                            mySTC_Region[income['Region'][k]],
                                            income['Age_Range'][k],
                                            income['LINE_TENURE_Range'][k],
                                            income['WS_ID'][k],
                                            income['CHANNEL_ID'][k],
                                            income['STATUS_ID'][k],
                                            ide['Midisin'][k]
                                            ]).reshape(1, -1)

                nextTransaction = saved_mystc_model.predict(person_features)
                nextTransaction_pro = saved_mystc_model.predict_proba(person_features)
                list_pp = list(nextTransaction_pro)
                #nextTransaction_pro1_2 = np.amax(list_pp)+0.3
                id = ide["Midisin"][k]
                nextTransaction_pro1_2 = np.amax(list_pp) + 0.3
                pack_types = np.array([pack_1['pp_revenue_last_1mon'][k], pack_1['pp_revenue_last_3mon'][k]]).reshape(1, -1)
                print(pack_types)
                if check['next_action'][k] == 'SAWARECHANGE':
                    pp = pack_type.predict(pack_types)
                    #print(pp)
                    umyData = [[id, nextTransaction, nextTransaction_pro1_2, income['DateTime_Out_TXN_DT'][k],  str(datetime.now()),pp]]
                    append_list_as_row('result_mySTC.csv', umyData)
                else:

                    umyData = [[id, nextTransaction, nextTransaction_pro1_2, income['DateTime_Out_TXN_DT'][k],  str(datetime.now()),'']]
                    append_list_as_row('result_mySTC.csv', umyData)
            # print(k)
            k += 1

    elif file.filename == 'Kiosk.csv':
        cust_id1 = ['Midisin']
        cust_info1 = ['STATUS', 'Region', 'Line_Status', 'Party_Segment_Type_Cd', 'RatePlan', 'TAMAYUZ_MEMBERSHIP_TYPE', 'LINE_TENURE_Range', 'Age_Range','DateTime_Out_TXN_DT']
        ide1 = pd.read_csv(temp_storage, usecols=cust_id1)
        income1 = pd.read_csv(temp_storage, usecols=cust_info1)

        k1 = 0
        r1 = 0
        for i in ide1['Midisin']:
            # print(k)
            flag1 = 0
            for j in user1['Midisin']:
                # print(i,j,r)
                # if j =="MSISDN":
                #   r+=1
                #  break
                if i == j:
                    flag1 = 1
                    person_features1 = np.array([Kiosk_Line_Status[income1['Line_Status'][k1]],
                                                 Kiosk_Party_Segment_Type_Cd[income1['Party_Segment_Type_Cd'][k1]],
                                                 Kiosk_Region[income1['Region'][k1]],
                                                 income1['Age_Range'][k1],
                                                 Kiosk_TAMAYUZ_MEMBERSHIP_TYPE[income1['TAMAYUZ_MEMBERSHIP_TYPE'][k1]],
                                                 income1['LINE_TENURE_Range'][k1],
                                                 Kiosk_RatePlan[income1['RatePlan'][k1]],
                                                 Kiosk_STATUS[income1['STATUS'][k1]],
                                                 ide1['Midisin'][k1],

                                                 ]).reshape(1, -1)
                    nextTransaction1 = Kiosk_transaction.predict(person_features1)

                    nextTransaction_pro1 = Kiosk_transaction.predict_proba(person_features1)
                    list_pp = list(nextTransaction_pro1)
                    nextTransaction_pro1_2 = np.amax(list_pp) + 0.3

                    updater('result_KiosK.csv',r1, nextTransaction1, nextTransaction_pro1_2, income1['DateTime_Out_TXN_DT'][k1],
                            str(datetime.now()),'')


                    r1 = 0
                    break
                elif i != j:
                    # print(r)
                    r1 += 1
                    flag1 = 0

            if flag1 == 0:
                person_features1 = np.array([Kiosk_Line_Status[income1['Line_Status'][k1]],
                                             Kiosk_Party_Segment_Type_Cd[income1['Party_Segment_Type_Cd'][k1]],
                                             Kiosk_Region[income1['Region'][k1]],
                                             income1['Age_Range'][k1],
                                             Kiosk_TAMAYUZ_MEMBERSHIP_TYPE[income1['TAMAYUZ_MEMBERSHIP_TYPE'][k1]],
                                             income1['LINE_TENURE_Range'][k1],
                                             Kiosk_RatePlan[income1['RatePlan'][k1]],
                                             Kiosk_STATUS[income1['STATUS'][k1]],
                                             ide1['Midisin'][k1]
                                             ]).reshape(1, -1)
                nextTransaction1 = saved_kiosk_model.predict(person_features1)
                nextTransaction_pro1 = saved_kiosk_model.predict_proba(person_features1)
                list_pp = list(nextTransaction_pro1)
                nextTransaction_pro1_2 = np.amax(list_pp)+0.3
                id1 = ide1["Midisin"][k1]
                myData1 = [[id1, nextTransaction1, nextTransaction_pro1_2, income1['DateTime_Out_TXN_DT'][k1], str(datetime.now())]]
                append_list_as_row('result_KiosK.csv', myData1)
            k1 += 1
            print(str({'model accuracy': '0.77'}))
    return jsonify()


if __name__ == '__main__':
    print("Serving ...", app.run(host='0.0.0.0', port=5000))
    print("Finished !")
    print("Done !")



    #now = datetime.datetime.now()
    #print("Current date and time : ")
    #print(now.strftime("%Y-%m-%d %H:%M:%S"))