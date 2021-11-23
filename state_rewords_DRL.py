import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections
import statistics
import scipy
import xlsxwriter
import csv

from xlsxwriter import Workbook
#############
#############
#cust_id = ["Midisin"]
#cust_info = ["Line_Status", "sa10_3", "sa20_7", "sa50_30", "sa100_90", "sa300_180", "sa_other"]
#row_data = pd.read_csv("major1.csv", usecols=cust_id)
#new_data = pd.read_csv("major1.csv", usecols=cust_info)
# s=pack["code"]
# s1= pack.iterrows()
# print(pack["Line_Status"][:])
# di.add(pack["Line_Status"])
# print(pack["code"][2])
#(Dict)

class my_dictionary(dict):

    def __init__(self):
        self = dict()
        # Function to add key:value

    def add(self, key, value):
        self[key] = value


class RL():
    g = 0
    def check_single(self1,sa, newpack, i,di_Sa):
        #print(sa)
        s_10 = str(['sawa10'])
        s_20 = str(['sawa20'])
        s_50 = str(['sawa50'])
        s_100 = str(['sawa100'])
        s_300 = str(['sawa300'])
        s_o = str(['sawaoth'])
        if sa==s_10 or sa=='sawa10':
            if sa == newpack:
                t = di_Sa[i][0]
                total_10 = t + 1
                d = di_Sa[i][2]
                s10_rechg = round(d * t)
                s10_rechg += 1
                s10_P = s10_rechg / total_10
                di_Sa[i][2] = s10_P
                di_Sa[i][0] = total_10

                # update recharge in his record
                # and update recharge in sa10 function
            else:
                t = di_Sa[i][0]
                total_10 = t + 1
                d = di_Sa[i][1]
                s10_chg = round(d * t)
                s10_chg += 1
                s10_P = s10_chg / total_10
                di_Sa[i][1] = s10_P
                di_Sa[i][0] = total_10

                # update change in his record
                # and update change in sa10 function

        elif sa==s_20 or sa=='sawa20':
            if sa == newpack:
                t = di_Sa[i][0]
                total_20 = t + 1
                d = di_Sa[i][2]
                s20_rechg = round(d * t)
                s20_rechg += 1
                s20_P = s20_rechg / total_20
                di_Sa[i][2] = s20_P
                di_Sa[i][0] = total_20

                # update recharge in his record
                # and update recharge in sa20 function

            else:
                t = di_Sa[i][0]
                total_20 = t + 1
                d = di_Sa[i][1]
                s20_chg = round(d * t)
                s20_chg += 1
                s20_P = s20_chg / total_20
                di_Sa[i][1] = s20_P
                di_Sa[i][0] = total_20

                # update change in his record
                # and update change in sa20 function

        elif sa==s_50 or sa=='sawa50':
            if sa == newpack:
                t = di_Sa[i][0]
                total_50 = t + 1
                d = di_Sa[i][2]
                s50_rechg = round(d * t)
                s50_rechg += 1
                s50_P = s50_rechg / total_50
                di_Sa[i][2] = s50_P
                di_Sa[i][0] = total_50

                # update recharge in his record
                # and update recharge in sa50 function


            else:
                t = di_Sa[i][0]
                total_50 = t + 1
                d = di_Sa[i][1]
                s50_chg = round(d * t)
                s50_chg += 1
                s50_P = s50_chg / total_50
                di_Sa[i][1] = s50_P
                di_Sa[i][0] = total_50

                # update change in his record
                # and update change in sa50 function


        elif sa==s_100 or sa=='sawa100':
            if sa == newpack:
                t = di_Sa[i][0]
                total_100 = t + 1
                d = di_Sa[i][2]
                s100_rechg = round(d * t)
                s100_rechg += 1
                s100_P = s100_rechg / total_100
                di_Sa[i][2] = s100_P
                di_Sa[i][0] = total_100

                # update recharge in his record
                # and update recharge in sa100 function


            else:
                t = di_Sa[i][0]
                total_100 = t + 1
                d = di_Sa[i][1]
                s100_chg = round(d * t)
                s100_chg += 1
                s100_P = s100_chg / total_100
                di_Sa[i][1] = s100_P
                di_Sa[i][0] = total_100

                # update change in his record
                # and update change in sa100 function


        elif sa==s_300 or sa=='sawa300':
            if sa == newpack:
                t = di_Sa[i][0]
                total_300 = t + 1
                d = di_Sa[i][2]
                s300_rechg = round(d * t)
                s300_rechg += 1
                s300_P = s300_rechg / total_300
                di_Sa[i][2] = s300_P
                di_Sa[i][0] = total_300

                # update recharge in his record
                # and update recharge in sa300 function
            else:
                t = di_Sa[i][0]
                total_300 = t + 1
                d = di_Sa[i][1]
                s300_chg = round(d * t)
                s300_chg += 1
                s300_P = s300_chg / total_300
                di_Sa[i][1] = s300_P
                di_Sa[i][0] = total_300

                # update change in his record
                # and update change in sa10 function


        elif  sa==s_o or sa=='sawaoth':
            # for other pack
            if sa == newpack:
                t = di_Sa[i][0]
                total_oth = t + 1
                d = di_Sa[i][2]
                soth_rechg = round(d * t)
                soth_rechg += 1
                soth_P = soth_rechg / total_oth
                di_Sa[i][2] = soth_P
                di_Sa[i][0] = total_oth

                # update recharge in his record
                # and update recharge in sawa other  function


            else:
                t = di_Sa[i][0]
                total_oth = t + 1
                # update change in his record
                # and update change in sawa other function
                d = di_Sa[i][1]
                soth_chg = round(d * t)
                soth_chg += 1
                soth_P = soth_chg / total_oth
                di_Sa[i][1] = soth_P
                di_Sa[i][0] = total_oth
    def rl(self1,file,file_source):
        col_list = ["Midisin"]
        reward_list = ["recharge", "double", "cancel", "change"]
        pack_code = ["Line_Status"]

        packs = ["sa10_3", "sa20_7", "sa50_30", "sa100_90", "sa300_180", "sa_other", "total", "recharge", "double",
                 "cancel", "change"]
        # data_form = ["sa_10?", "sa_20?", "sa_50?", "sa_100?", "sa_300?", "sa_oth?", "total", "recharge", "double", "cancel",
        # "change"]
        #data = pd.read_csv(file_source)
        data_predict = ["R_L_EXPERIENCE", "Y_indicator"]
        predict = pd.read_csv(file_source, usecols=data_predict)
        user = pd.read_csv(file_source, usecols=col_list)
        #pre_packs = pd.read_csv(file_source, usecols=packs)
        reward = pd.read_csv(file_source, usecols=reward_list)
        pack = pd.read_csv(file_source, usecols=pack_code)
        state = pd.read_csv(file_source, usecols=packs)
        state_reward = pd.read_csv(file_source, usecols=packs)
        g = 0
        Dict = my_dictionary()
        Dict = collections.defaultdict(list)

            #  print(pack["code"][g])
            ### m=pack["code"][g]
            # if pack["code"][g]==0:
            #       g=g+1
        global cu, cont
        cust_id = ["Midisin"]
        cust_info = ["Line_Status","sa10_3", "sa20_7", "sa50_30", "sa100_90", "sa300_180", "sa_other"]
        row_data = pd.read_csv(file, usecols=cust_id)
        new_data = pd.read_csv(file, usecols=cust_info)
        k = 0
        r = 0

        # print(row_data["Midisin"])
        # print(row_data["Midisin"])
        # print(row_data["Midisin"])
        for i in row_data["Midisin"]:
            # if  i=="Midisin" or "nan":
            #   k+=1
            #print(k)
            # print(i)
            flag=0
            for j in user["Midisin"]:
                # print(i,j,r)
                # if j =="Midisin":
                #   r+=1
                #  break


                if i == j:
                    flag=1

                    di_Sa = my_dictionary()
                    di_Sa = collections.defaultdict(list)
                   # print(r)
                    di_Sa.setdefault(i, [0, 0, 0, 0, 0])
                    pre_re = ["total", "change", "recharge", "cancel", "double"]
                    pre_re1 = pd.read_csv(file_source, usecols=pre_re)
                    di_Sa[i][0] = pre_re1["total"][r]
                    di_Sa[i][1] = pre_re1["change"][r]
                    di_Sa[i][2] = pre_re1["recharge"][r]
                    di_Sa[i][3] = pre_re1["cancel"][r]
                    di_Sa[i][4] = pre_re1["double"][r]
                    #print(di_Sa)
                    #print(di_Sa)
                    s10 = 0
                    s20 = 0
                    s50 = 0
                    s100 = 0
                    s300 = 0
                    s1 = 0
                    cont = 6
                    if new_data["sa10_3"][k] < 28:
                        s10 = 10
                    else:
                        cont -= 1
                    if new_data["sa20_7"][k] < 28:
                        s20 = 20
                    else:
                        cont -= 1
                    if new_data["sa50_30"][k] < 28:
                        s50 = 50
                    else:
                        cont -= 1
                    if new_data["sa100_90"][k] < 28:
                        s100 = 100
                    else:
                        cont -= 1
                    if new_data["sa300_180"][k] < 28:
                        s300 = 300
                    else:
                        cont -= 1
                    if new_data["sa_other"][k] < 28:
                        s1 = 1
                    else:
                        cont -= 1
                    cu = {"sawa10": s10, "sawa20": s20, "sawa50": s50, "sawa100": s100, "sawa300": s300, "sawaoth": s1}
                    #print(cu)
                    Dict.clear()
                    if (state["sa10_3"][r]) <= 28:
                        Dict.setdefault(user["Midisin"][r], [])
                        Dict[user["Midisin"][r]].append("sawa10")
                        if (state["sa20_7"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa20")
                        if (state["sa50_30"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa50")
                        if (state["sa100_90"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa100")
                        if (state["sa300_180"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa300")
                        if (state["sa_other"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawaoth")
                    elif state["sa20_7"][r] <= 28:
                        Dict.setdefault(user["Midisin"][r], [])
                        Dict[user["Midisin"][r]].append("sawa20")
                        if (state["sa50_30"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa50")
                        if (state["sa100_90"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa100")
                        if (state["sa300_180"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa300")
                        if (state["sa_other"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawaoth")
                    elif state["sa50_30"][r] <= 28:
                        Dict.setdefault(user["Midisin"][r], [])
                        Dict[user["Midisin"][r]].append("sawa20")
                        if (state["sa100_90"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa100")
                        if (state["sa300_180"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa300")
                        if (state["sa_other"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawaoth")
                    elif state["sa100_90"][r] <= 28:
                        Dict.setdefault(user["Midisin"][r], [])
                        Dict[user["Midisin"][r]].append("sawa20")
                        if (state["sa300_180"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawa300")
                        if (state["sa_other"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawaoth")
                    elif state["sa300_180"][r] <= 28:
                        Dict.setdefault(user["Midisin"][r], [])
                        Dict[user["Midisin"][r]].append("sawa20")
                        if (state["sa_other"][r]) <= 28:
                            Dict.setdefault(user["Midisin"][r], [])
                            Dict[user["Midisin"][r]].append("sawaoth")
                    elif state["sa_other"][r] <= 28:
                        Dict.setdefault(user["Midisin"][r], [])
                        Dict[user["Midisin"][r]].append("sawa20")
                    else:
                        Dict.setdefault(user["Midisin"][r], [])
                        Dict[user["Midisin"][r]].append("disable")
                    if cont == 0 :
                        if sum([len(Dict[i])]) == 1:
                            # checking which pack among six packs
                            pa = Dict[i]
                            s_10 = str(['sawa10'])
                            s_20 = str(['sawa20'])
                            s_50 = str(['sawa50'])
                            s_100 = str(['sawa100'])
                            s_300 = str(['sawa300'])
                            s_o = str(['sawaoth'])
                            if pa==s_10:
                                t = di_Sa[i][0]
                                total_10 = t + 1
                                d = di_Sa[i][3]
                                s10_cle = round(d * t)
                                s10_cle += 1
                                s10_P = s10_cle / total_10
                                di_Sa[i][3] = s10_P
                                di_Sa[i][0] = total_10

                                # update cancel in his record
                                # and update cancel in sa10 function
                            elif pa==s_20:
                                t = di_Sa[i][0]
                                total_20 = t + 1
                                d = di_Sa[i][3]
                                s20_cle = round(d * t)
                                s20_cle += 1
                                s20_P = s20_cle / total_20
                                di_Sa[i][3] = s20_P
                                di_Sa[i][0] = total_20

                                # update cancel in his record
                                # and update cancel in sa10 function
                            elif pa==s_50:
                                t = di_Sa[i][0]
                                total_50 = t + 1
                                d = di_Sa[i][3]
                                s50_cle = round(d * t)
                                s50_cle += 1
                                s50_P = s50_cle / total_50
                                di_Sa[i][3] = s50_P
                                di_Sa[i][0] = total_50

                                # update cancel in his record
                                # and update cancel in sa10 function

                            elif pa==s_100:
                                t = di_Sa[i][0]
                                total_100 = t + 1
                                d = di_Sa[i][3]
                                s100_cle = round(d * t)
                                s100_cle += 1
                                s100_P = s100_cle / total_100
                                di_Sa[i][3] = s100_P
                                di_Sa[i][0] = total_100

                                # update cancel in his record
                                # and update cancel in sa10 function

                            elif pa==s_300:
                                t = di_Sa[i][0]
                                total_300 = t + 1
                                d = di_Sa[i][3]
                                s300_cle = round(d * t)
                                s300_cle += 1
                                s300_P = s300_cle / total_300
                                di_Sa[i][3] = s300_P
                                di_Sa[i][0] = total_300

                                # update cancel in his record
                                # and update cancel in sa10 function

                            elif pa==s_o:
                                t = di_Sa[i][0]
                                total_oth = t + 1
                                d = di_Sa[i][3]
                                soth_cle = round(d * t)
                                soth_cle += 1
                                soth_P = soth_cle / total_oth
                                di_Sa[i][3] = soth_P
                                di_Sa[i][0] = total_oth
                            # update cancel in his record
                            # and update cancel in sa10 function
                        self1.updater1(file_source, r, k, di_Sa, i,file)
                    elif cont>=3:
                        self1.updater2(file_source, r, k, di_Sa, i,file)


                        # that means that the customer dont have any packs
                        # let's checking previous status of his
                        # if Dict[i] == "disable":
                        # k += 1
                    elif cont < 3 and cont > 0:
                        di=self1.check_newpack(cont, Dict, cu, i,di_Sa)
                        #print(Dict[i])
                        #print(di)
                        if cont != 0:
                            R_L_EXPERIENCE, Y_indicator, u = cc.prediction(di_Sa, i, di,file_source)
                            self1.updater(file_source, r, k, di_Sa, i, R_L_EXPERIENCE, Y_indicator,file,u)
                        else:
                            self1.updater1(file_source, r, k, di_Sa, i,file)
                    del di_Sa[i]

                    r = 0
                    cont = 0
                    break

                elif  i != j:
                    #print(r)
                    r += 1
                    flag=0
            if flag==0:
                # print(r)
                initil = 0
                change = np.random.uniform(low=0, high=0.3)
                recharge = np.random.uniform(low=0, high=0.7)
                cancel = np.random.uniform(low=0, high=0.1)
                double = np.random.uniform(low=0, high=0.1)
                id = row_data["Midisin"][k]
                stat = new_data["Line_Status"][k]
                b1 = new_data["sa10_3"][k]
                b2 = new_data["sa20_7"][k]
                b3 = new_data["sa50_30"][k]
                b4 = new_data["sa100_90"][k]
                b5 = new_data["sa300_180"][k]
                b6 = new_data["sa_other"][k]
                R_L_EXPERIENCE=0
                Y_indicator=0
                u="recharge"
                myData = [[id, stat, b1, b2, b3, b4, b5, b6, initil, change, recharge, cancel, double,
                           '', '']]
                self1.append_list_as_row(file_source, myData)
            #print(k)
            k += 1
            #

        #return R_L_EXPERIENCE, Y_indicator, u

    def check_newpack(self1,cont, Dict, cu, i,di_Sa):
        # print(Dict[i])
        di = []
        di.clear()
        if cont == 1:
            for k, j in cu.items():
                if j != 0:
                    di.append(k)
                    #di=newpack
            if sum([len(Dict[i])]) == 1:
                sa = Dict[i]
                self1.check_single(sa, di, i,di_Sa)

            elif sum([len(Dict[i])]) == 2:
                sa, ma = Dict[i][:]

                self1.check_single(sa, di, i,di_Sa)
                self1.check_single(ma, di, i,di_Sa)
            elif sum([len(Dict[i])]) == 3:
                sa, ma, ta = Dict[i][:]
                self1.check_single(sa, di, i,di_Sa)
                self1.check_single(ma, di, i,di_Sa)
                self1.check_single(ta, di, i,di_Sa)
        elif cont == 2:
            for k, j in cu.items():
                if j != 0:
                    di.append(k)

            di_Sa[i][:] =self1.dobl(di, i,di_Sa)

            if sum([len(Dict[i])]) == 1:
                sa = Dict[i]
                for q in di:
                    if q == sa:
                        self1.check_single(sa, q, i,di_Sa)
            elif sum([len(Dict[i])]) == 2:
                sa, ma = Dict[i][:]
                for x in di:
                    if x == sa:
                        self1.check_single(sa, x, i,di_Sa)
                    if x == ma:
                        self1.check_single(ma, x, i,di_Sa)
            elif sum([len(Dict[i])]) == 3:
                sa, ma, ta = Dict[i][:]
                for x in di:
                    if x == sa:
                        self1.check_single(sa, x, i,di_Sa)
                    if x == ma:
                        self1.check_single(ma, x, i,di_Sa)
                    if x == ta:
                        self1.check_single(ma, x, i,di_Sa)
        return di

    def dobl(self1,di, i,di_Sa):
        for iss in di:
            if iss.endswith("a10"):
                t = di_Sa[i][0]
                total_10 = t + 1
                d = di_Sa[i][4]
                s10_dobl = round(d * t)
                s10_dobl += 1
                s10_P = s10_dobl / total_10
                di_Sa[i][4] = s10_P
                di_Sa[i][0] = total_10

            elif iss.endswith("a20"):
                t = di_Sa[i][0]
                total_20 = t + 1
                d = di_Sa[i][4]
                s20_dobl = round(d * t)
                s20_dobl += 1
                s20_P = s20_dobl / total_20
                di_Sa[i][4] = s20_P
                di_Sa[i][0] = total_20

            elif iss.endswith("a50"):
                t = di_Sa[i][0]
                total_50 = t + 1
                d = di_Sa[i][4]
                s50_dobl = round(d * t)
                s50_dobl += 1
                s50_P = s50_dobl / total_50
                di_Sa[i][4] = s50_P
                di_Sa[i][0] = total_50

            elif iss.endswith("100"):
                t = di_Sa[i][0]
                total_100 = t + 1
                d = di_Sa[i][4]
                s100_dobl = round(d * t)
                s100_dobl += 1
                s100_P = s100_dobl / total_100
                di_Sa[i][4] = s100_P
                di_Sa[i][0] = total_100

            elif iss.endswith("300"):
                t = di_Sa[i][0]
                total_300 = t + 1
                d = di_Sa[i][4]
                s300_dobl = round(d * t)
                s300_dobl += 1
                s300_P = s300_dobl / total_300
                di_Sa[i][4] = s300_P
                di_Sa[i][0] = total_300




            elif iss.endswith("oth"):
                t = di_Sa[i][0]
                total_oth = t + 1
                d = di_Sa[i][4]
                soth_dobl = round(d * t)
                soth_dobl += 1
                soth_P = soth_dobl / total_oth
                di_Sa[i][4] = soth_P
                di_Sa[i][0] = total_oth
        return di_Sa[i][:]

    def updater2(self1,filename, r, k, di_Sa, i,ww):
        cust_info = ["Line_Status", "sa10_3", "sa20_7", "sa50_30", "sa100_90", "sa300_180", "sa_other"]
        new_data = pd.read_csv(ww, usecols=cust_info)
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]
            # print(readData[r]["Midisin"])
            readData[r]["Line_Status"] = new_data["Line_Status"][k]
            readData[r]["sa10_3"] = new_data["sa10_3"][k]
            readData[r]["sa20_7"] = new_data["sa20_7"][k]
            readData[r]["sa50_30"] = new_data["sa50_30"][k]
            readData[r]["sa100_90"] = new_data["sa100_90"][k]
            readData[r]["sa300_180"] = new_data["sa300_180"][k]
            readData[r]["sa_other"] = new_data["sa_other"][k]
            readData[r]["total"] = di_Sa[i][0] + 1
            readData[r]["change"] = di_Sa[i][1]
            readData[r]["recharge"] = di_Sa[i][2]
            readData[r]["cancel"] = di_Sa[i][3]
            readData[r]["double"] = di_Sa[i][4]

            # print(readData)
        readHeader = readData[r].keys()
        self1.writer(readHeader, readData, filename, "update")

    def updater1(self1,filename, r, k, di_Sa, i,ww):
        cust_info = ["Line_Status", "sa10_3", "sa20_7", "sa50_30", "sa100_90", "sa300_180", "sa_other"]
        new_data = pd.read_csv(ww, usecols=cust_info)
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]
            # print(readData[r]["Midisin"])
            readData[r]["Line_Status"] = 'Inactive'
            readData[r]["sa10_3"] = new_data["sa10_3"][k]
            readData[r]["sa20_7"] = new_data["sa20_7"][k]
            readData[r]["sa50_30"] = new_data["sa50_30"][k]
            readData[r]["sa100_90"] = new_data["sa100_90"][k]
            readData[r]["sa300_180"] = new_data["sa300_180"][k]
            readData[r]["sa_other"] = new_data["sa_other"][k]
            readData[r]["total"] = di_Sa[i][0]
            readData[r]["change"] = di_Sa[i][1]
            readData[r]["recharge"] = di_Sa[i][2]
            readData[r]["cancel"] = di_Sa[i][3]
            readData[r]["double"] = di_Sa[i][4]

            # print(readData)
        readHeader = readData[r].keys()
        self1.writer(readHeader, readData, filename, "update")

    def updater(self1,filename, r, k, di_Sa, i, R_L_EXPERIENCE, Y_indicator,ww,s):
        cust_info = ["Line_Status", "sa10_3", "sa20_7", "sa50_30", "sa100_90", "sa300_180", "sa_other"]
        new_data = pd.read_csv(ww, usecols=cust_info)
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]
            # print(readData[r]["Midisin"])
            readData[r]["Midisin"] = i
            readData[r]["Line_Status"] = new_data["Line_Status"][k]
            readData[r]["sa10_3"] = new_data["sa10_3"][k]
            readData[r]["sa20_7"] = new_data["sa20_7"][k]
            readData[r]["sa50_30"] = new_data["sa50_30"][k]
            readData[r]["sa100_90"] = new_data["sa100_90"][k]
            readData[r]["sa300_180"] = new_data["sa300_180"][k]
            readData[r]["sa_other"] = new_data["sa_other"][k]
            readData[r]["total"] = di_Sa[i][0]
            readData[r]["change"] = di_Sa[i][1]
            readData[r]["recharge"] = di_Sa[i][2]
            readData[r]["cancel"] = di_Sa[i][3]
            readData[r]["double"] = di_Sa[i][4]
            readData[r]["R_L_EXPERIENCE"] = R_L_EXPERIENCE
            readData[r]["Y_indicator"] = Y_indicator
            readData[r]["next_action"] = s
            # print(readData)
        readHeader = readData[r].keys()
        self1.writer(readHeader, readData, filename, "update")

    def writer(self1,header, data, filename, option):
        with open(filename, "w", newline="") as csvfile:
            if option == "write":

                movies = csv.writer(csvfile)
                movies.writerow(header)
                for x in data:
                    movies.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")

    def append_list_as_row(self1,storage, list_of_elem):
        # Open file in append mode
        with open(storage, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            # csv_writer.writerow(f)
            csv_writer.writerows(list_of_elem)
class DRL(object):
    def __init__(self):
        first = True
        N = 4
        D = 1  # DRL
        HD1 = 4
        HD2 = 4
        K = 1
        if first == True:
            first = False
            self.w = self.initilization(D, HD1)  # input_weights
            self.b = np.random.randn(HD1)  # bias_HD1
            self.p = self.initilization(HD2, 1)  # HD2_weights
            self.f = np.random.randn(K)  # bias_output

    def sigmoid(self, a):
        return 1 / (1 + np.exp(-a))

    def prediction_rate(self, Y, P,n):
        s=float(Y[n]/P[n])*100
        return s



    def forward(self,x):
        #    w,b,v,,c,p,f=initilization()
        a = x.dot(self.w) + self.b
        z = self.sigmoid(a)
        y = z.dot(self.p) + self.f
        Y_hat = self.sigmoid(y)
        return Y_hat,z
    def check(self, s,h):
       # print(s)
        if len(s) == 1:
            c= self.t(s,h)
            #print(c)
        elif len(s) == 2:
            si, mi = s[:]
            s1 = self.t(si,h)
            s2 = self.t(mi,h)
            c= self.mean_d(s1, s2)
            #print(c)
        elif len(s) == 3:
            si, mi, zi = s[:]
            s1 = self.t(si,h)
            s2 = self.t(mi,h)
            s3 = self.t(zi,h)
            c = self.mean_t(s1, s2, s3)
           # print(c)
        return c
    def training(self, Y_indicator, T_indicator, z, learning_rate, x):
        grad_p = (T_indicator - Y_indicator).T.dot(z)
        grad_f = np.sum((T_indicator - Y_indicator), axis=0)
        self.p -= (learning_rate * grad_p.T)
        self.f -=  learning_rate * grad_f
        dz1 = np.outer(T_indicator - Y_indicator, self.p) * z * (1 - z)
        grad_w =x.T.dot(dz1)
        grad_b=dz1.sum(axis=0)
        self.w -= learning_rate * grad_w
        self.b -= learning_rate * grad_b
        #print(self.b)
        return self.w, self.b, self.p, self.f

   # def cost(self, T, Y):
    #    tot = -T * np.log(Y)
     #   return tot.sum()

    def NN(self, f, y):
        x=0
        #print(f[y])
        #   if z.endswith("sa10") for z in Dict[i].iterrows(): x1=1
        #print(f)
        HD2 = 4
        #print(x.shape)
        Y = np.array([HD2, 1])
        return Y

    def prediction(self,m, e, s,h):
        #print(s)
        d = self.check(s,h)
        #print(s)
        j=np.array([d])
        t=j.T


        # learning_rate = 0.001
        # print("a")
        #print(m[e])
        # print(Y_indicator)
        # TARGET checking............................


        x1 = m[e][1]
        x2 = m[e][2]
        x3 = m[e][3]
        x4 = m[e][4]

        x = np.vstack([x1,x2,x3,x4])
        T=self.mean_d(t,x)

        is_all_zero = not np.any(x)
        # .....................................
        if not is_all_zero:
            learning_rate = 0.0001
            epoch = 10
            while (epoch != 0):
                Y_indicator,z_P = self.forward(x)
                self.w, self.b, self.p, self.f = self.training(Y_indicator, T, z_P, learning_rate, x)
                epoch -= 1
            cost = []

            R_L_EXPERIENCE = self.prediction_rate(Y_indicator,T,np.argmax(T))
            # print("prediction_rate:", R_L_EXPERIENCE)
            #c = self.cost(Y_indicator, T)
            #cost.append(c)
            w=np.argmax(Y_indicator)
            if w==  0: action= "SAWARECHANGE"
            if w == 1: action = "recharge"
            if w == 2: action = "cancel"
            if w == 3: action = "double"
        return R_L_EXPERIENCE,max(Y_indicator)*100,action

    def t(self,s,ss):
        packs = ["sa10_3", "sa20_7", "sa50_30", "sa100_90", "sa300_180", "sa_other", "total", "recharge", "double",
                 "cancel", "change"]
        state_reward = pd.read_csv(ss, usecols=packs)
        si = str(s)
        # print(si)
        s_10 = str(['sawa10'])
        s_20 = str(['sawa20'])
        s_50 = str(['sawa50'])
        s_100 = str(['sawa100'])
        s_300 = str(['sawa300'])
        s_o = str(['sawaoth'])

        if si == s_10 or si == 'sawa10':
            _, sw = self.calclute_Stat_sa_10(state_reward)

        if si == s_20 or si == 'sawa20':
            _, sw = self.calclute_Stat_sa_20(state_reward)

        if si == s_50 or si == 'sawa50':
            _, sw = self.calclute_Stat_sa_50(state_reward)

        if si == s_100 or si == 'sawa100':
            _, sw = self.calclute_Stat_sa_100(state_reward)

        if si == s_300 or si == 'sawa300':
            _, sw = self.calclute_Stat_sa_300(state_reward)

        if si == s_o or si == 'sawaoth':
            _, sw = self.calclute_Stat_sa_oth(state_reward)

        return sw

    def mean_d(self,s1, s2):
        t1 = (s1[0] + s2[0]) / 2
        # print(t1,s1[0],s2[0])
        t2 = (s1[1] + s2[1]) / 2
        t3 = (s1[2] + s2[2]) / 2
        t4 = (s1[3] + s2[3]) / 2
        re = [t1, t2, t3, t4]
        return re

    def mean_t(self,s1, s2, s3):
        re = [s1[0] + s2[0] + s3[0] / 3, s1[1] + s2[1] + s3[1] / 3, s1[2] + s2[2] + s3[2] / 3,
              s1[3] + s2[3] + s3[3] / 3]
        return re

    def initilization(self,m, s):
        return np.random.randn(m, s)

    def calclute_Stat_sa_10(self,data):
        'sa_10 mean value for each pack'
        df = data[['recharge', 'sa10_3']]
        recharge_greater0 = df[df["sa10_3"] <= 28]
        mean_recharge = recharge_greater0['recharge'].mean(axis=0, skipna=True)
        df2 = data[['double', 'sa10_3']]
        double_greater0 = df2[df2["sa10_3"] <= 28]
        mean_double = double_greater0['double'].mean(axis=0, skipna=True)
        df3 = data[['cancel', 'sa10_3']]
        cancel_greater0 = df3[df3["sa10_3"] <= 28]
        cancel_double = cancel_greater0['cancel'].mean(axis=0, skipna=True)
        df4 = data[['change', 'sa10_3']]
        change_greater0 = df4[df4["sa10_3"] <= 28]
        change_double = change_greater0['change'].mean(axis=0, skipna=True)
        sa_10 = {"change_double": change_double, "mean_recharge": mean_recharge, "cancel_double": cancel_double,
                 "mean_double": mean_double}
        sa_10_2 = [change_double, mean_recharge, cancel_double, mean_double]
        return sa_10, sa_10_2

    def calclute_Stat_sa_20(self,data):
        'sa_20 mean value for each puck'
        df = data[['recharge', 'sa20_7']]
        recharge_greater0 = df[df["sa20_7"] <= 28]
        mean_recharge = recharge_greater0['recharge'].mean(axis=0, skipna=True)
        df2 = data[['double', 'sa20_7']]
        double_greater0 = df2[df2["sa20_7"] <= 28]
        mean_double = double_greater0['double'].mean(axis=0, skipna=True)
        df3 = data[['cancel', 'sa20_7']]
        cancel_greater0 = df3[df3["sa20_7"] <= 28]
        cancel_double = cancel_greater0['cancel'].mean(axis=0, skipna=True)
        df4 = data[['change', 'sa20_7']]
        change_greater0 = df4[df4["sa20_7"] <= 28]
        change_double = change_greater0['change'].mean(axis=0, skipna=True)
        sa_20 = {"change_double": change_double, "mean_recharge": mean_recharge, "cancel_double": cancel_double,
                 "mean_double": mean_double}
        sa_20_2 = [change_double, mean_recharge, cancel_double, mean_double]
        return sa_20, sa_20_2

    def calclute_Stat_sa_50(self,data):
        'sa_50 mean value for each puck'
        df = data[['recharge', 'sa50_30']]
        recharge_greater0 = df[df["sa50_30"] <= 28]
        mean_recharge = recharge_greater0['recharge'].mean(axis=0, skipna=True)
        df2 = data[['double', 'sa50_30']]
        double_greater0 = df2[df2["sa50_30"] <= 28]
        mean_double = double_greater0['double'].mean(axis=0, skipna=True)
        df3 = data[['cancel', 'sa50_30']]
        cancel_greater0 = df3[df3["sa50_30"] <= 28]
        cancel_double = cancel_greater0['cancel'].mean(axis=0, skipna=True)
        df4 = data[['change', 'sa50_30']]
        change_greater0 = df4[df4["sa50_30"] <= 28]
        change_double = change_greater0['change'].mean(axis=0, skipna=True)
        sa_50 = {"change_double": change_double, "mean_recharge": mean_recharge, "cancel_double": cancel_double,
                 "mean_double": mean_double}
        sa_50_2 = [change_double, mean_recharge, cancel_double, mean_double]
        return sa_50, sa_50_2

    def calclute_Stat_sa_100(self,data):
        'sa_100 mean value for each puck'
        df = data[['recharge', 'sa100_90']]
        recharge_greater0 = df[df["sa100_90"] <= 28]
        mean_recharge = recharge_greater0['recharge'].mean(axis=0, skipna=True)
        df2 = data[['double', 'sa100_90']]
        double_greater0 = df2[df2["sa100_90"] <= 28]
        mean_double = double_greater0['double'].mean(axis=0, skipna=True)
        df3 = data[['cancel', 'sa100_90']]
        cancel_greater0 = df3[df3["sa100_90"] <= 28]
        cancel_double = cancel_greater0['cancel'].mean(axis=0, skipna=True)
        df4 = data[['change', 'sa100_90']]
        change_greater0 = df4[df4["sa100_90"] <= 28]
        change_double = change_greater0['change'].mean(axis=0, skipna=True)
        sa_100 = {"change_double": change_double, "mean_recharge": mean_recharge, "cancel_double": cancel_double,
                  "mean_double": mean_double}
        sa_100_2 = [change_double, mean_recharge, cancel_double, mean_double]
        return sa_100, sa_100_2

    def calclute_Stat_sa_300(self,data):
        'sa_300 mean value for each puck'
        df = data[['recharge', 'sa300_180']]
        recharge_greater0 = df[df["sa300_180"] <= 28]
        mean_recharge = recharge_greater0['recharge'].mean(axis=0, skipna=True)
        df2 = data[['double', 'sa300_180']]
        double_greater0 = df2[df2["sa300_180"] <= 28]
        mean_double = double_greater0['double'].mean(axis=0, skipna=True)
        df3 = data[['cancel', 'sa300_180']]
        cancel_greater0 = df3[df3["sa300_180"] <= 28]
        cancel_double = cancel_greater0['cancel'].mean(axis=0, skipna=True)
        df4 = data[['change', 'sa300_180']]
        change_greater0 = df4[df4["sa300_180"] <= 28]
        change_double = change_greater0['change'].mean(axis=0, skipna=True)
        sa_300 = {"change_double": change_double, "mean_recharge": mean_recharge, "cancel_double": cancel_double,
                  "mean_double": mean_double}
        sa_300_2 = [change_double, mean_recharge, cancel_double, mean_double]
        return sa_300, sa_300_2

    def calclute_Stat_sa_oth(self,data):
        'sa_oth mean value for each puck'
        df = data[['recharge', 'sa_other']]
        recharge_greater0 = df[df["sa_other"] <= 28]
        mean_recharge = recharge_greater0['recharge'].mean(axis=0, skipna=True)
        df2 = data[['double', 'sa_other']]
        double_greater0 = df2[df2["sa_other"] <= 28]
        mean_double = double_greater0['double'].mean(axis=0, skipna=True)
        df3 = data[['cancel', 'sa_other']]
        cancel_greater0 = df3[df3["sa_other"] <= 28]
        cancel_double = cancel_greater0['cancel'].mean(axis=0, skipna=True)
        df4 = data[['change', 'sa_other']]
        change_greater0 = df4[df4["sa_other"] <= 28]
        change_double = change_greater0['change'].mean(axis=0, skipna=True)
        sa_oth = {"change_double": change_double, "mean_recharge": mean_recharge, "cancel_double": cancel_double,
                  "mean_double": mean_double}
        sa_oth_2 = [change_double, mean_recharge, cancel_double, mean_double]
        return sa_oth, sa_oth_2




cc = DRL()
dd=RL()

#print(a)






