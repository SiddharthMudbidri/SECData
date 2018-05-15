# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 10:46:05 2018

@author: siddh
"""

from urllib.request import urlopen
import zipfile
import json
import csv
import pandas as pd
import collections
import numpy as np

fq = pd.DataFrame([])
def converttoCSV():
    txt_file = r"sub.txt"
    # to create files if not already present
    csv_file = "sub.csv"
    in_txt = csv.reader(open(txt_file, "r"), delimiter='\t')
    out_csv = csv.writer(open(csv_file, 'w', newline=''))
    out_csv.writerows(in_txt)
    txt_file = r"num.txt"
    csv_file = r"num.csv"
    in_txt = csv.reader(open(txt_file, "r"), delimiter='\t')  # converting
    out_csv = csv.writer(open(csv_file, 'w'))
    out_csv.writerows(in_txt)


def joinCSV():
    f = open("result.csv", "w+")  # creating the result.csv file for holding the merged content
    df1 = pd.read_csv("sub.csv", low_memory=False)
    df = pd.read_csv("num.csv", low_memory=False)  # so that it does'nt crash
    result = df1.merge(df, on="adsh")
    result.to_csv("result.csv")


def converttodict():
    print("in convertotdict function")
    new_data = []
    new_data1 = []
    with open('sub.csv') as f:
        reader = csv.DictReader(f)
        dict1 = reader

        # for row in dict1:
        #    print(row['adsh'])
        keys = ['adsh', 'cik', 'name']
        new_data = [dict((k, d[k]) for k in keys) for d in dict1]
        df1 = pd.DataFrame.from_dict(new_data)

    #  print(new_data)
    with open('num.csv') as f:
        reader = csv.DictReader(f)
        dict1 = reader
        keys = ['adsh', 'tag', 'value', 'qtrs','ddate']
        new_data1 = [dict((k, d[k]) for k in keys) for d in dict1]  #converting to dictionary
    df2 = pd.DataFrame.from_dict(new_data1)
    df3 = pd.merge(df1, df2, on=['adsh'])  #join the tables
    print("now merging")
    index = i = fi = 0
    flagNI2017 = 0
    flagNI2016 = 0
    flagassets2017 = 0
    flagassets2016 = 0

    flagliabilities2016 = 0
    flagliabilities2017 = 0

    flagCA2017 = 0
    flagCL2017 = 0

    flagCA2016 = 0
    flagCL2016 = 0

    flagdep = 0
    flagII = 0
    flagshare = 0
    flagsales2017 = 0
    flagsales2016 = 0

    while index <= 2281511:
        index = i + 1
        cname = df3.iloc[index]['name']

        if df3.iloc[i]['name'] == cname:

            if df3.iloc[i]['ddate'] == '20170930':

                if df3.iloc[i]['tag'].lower() == 'netincomeloss' or df3.iloc[index]['tag'].lower() == 'profitloss': # check for tag
                    if df3.iloc[i]['qtrs']=='3':
                        flagNI2017 = flagNI2017+ 1
                        if flagNI2017 == 1:
                            NetIncome2017 = df3.iloc[i]['value']
                            if NetIncome2017 =='':
                                NetIncome2017 = 0
                            NetIncome2017 = float(NetIncome2017)
                            cname = df3.iloc[index]['name']
                            CompanyNameList.append(cname)
                            netincomelist.append(NetIncome2017)


                elif df3.iloc[i]['tag'].lower() == 'assets':
                    if df3.iloc[i]['qtrs'] == '0':
                        flagassets2017  =  flagassets2017 + 1  #NetIncome = profitloss,netincomeloss
                        if flagassets2017 == 1:
                            Assets2017 = df3.iloc[i]['value']
                            if Assets2017 == '':
                                Assets2017 = 0
                            Assets2017 = float(Assets2017)
                            assets2017list.append(Assets2017)

                elif df3.iloc[i]['tag'].lower() == 'salesrevenueservicesnet' or df3.iloc[i]['tag'].lower() == 'refiningandmarketingrevenue' or df3.iloc[i]['tag'].lower() == 'oilandgasrevenue' or df3.iloc[i]['tag'].lower() == 'naturalgasmidstreamrevenue' or df3.iloc[i]['tag'].lower() == 'oilandgasrevenue' or df3.iloc[i]['tag'].lower() == 'regulatedandunregulatedoperatingrevenue' or df3.iloc[i]['tag'].lower() == 'interestanddividendincomeoperating' or df3.iloc[i]['tag'].lower() == 'noninterestincome' or df3.iloc[i]['tag'].lower() == 'financingrevenueandnotherinterestincomenet' or df3.iloc[i]['tag'].lower() == 'realestaterevenuenet' or df3.iloc[i]['tag'].lower() == 'healthcareorganizationrevenuenetofpatientservicerevenueprovisions' :

                        flagsales2017  =  flagsales2017 + 1  #NetIncome = profitloss,netincomeloss
                        if flagsales2017 == 1:
                            Sales2017 = df3.iloc[i]['value']
                            if Sales2017 == '':
                                Sales2017 = 0
                            Sales2017 = float(Sales2017)
                            Sales2017list.append(Sales2017)




                elif df3.iloc[i]['tag'].lower() == 'liabilities':
                    Liabilities2017 = df3.iloc[i]['value']
                    flagliabilities2017 = flagliabilities2017 + 1
                    if flagliabilities2017 == 1:
                        if Liabilities2017 == '':
                            Liabilities2017 = 0
                        Liabilities2017 = float(Liabilities2017)
                        liabilities2017list.append(Liabilities2017)
                    # if else to access tag values
                elif df3.iloc[i]['tag'].lower() == 'assetscurrent':
                        flagCA2017 = flagCA2017 + 1
                        if flagCA2017 == 1:
                            CurrentAssets2017 = df3.iloc[i]['value']
                            if CurrentAssets2017 == '':
                             CurrentAssets2017 = 0
                            CurrentAssets2017 = float(CurrentAssets2017)
                            CA2017list.append(CurrentAssets2017)

                elif df3.iloc[i]['tag'].lower() == 'liabilitiescurrent':

                    flagCL2017 = flagCL2017 + 1
                    if flagCL2017 == 1:
                        CurrentLiabilities2017 = df3.iloc[i]['value']
                        if CurrentLiabilities2017 == '':
                            CurrentLiabilities2017 = 0
                        CurrentLiabilities2017 = float(CurrentLiabilities2017)
                        CL2017list.append(CurrentLiabilities2017)

                elif df3.iloc[i]['tag'].lower() == 'commonstockdividendspersharedeclared':
                   flagshare = flagshare + 1
                   if flagshare == 1:
                    Share2017 = df3.iloc[i]['value']

                    if Share2017 == '':
                          Share2017= 0
                    Share2017 = float(Share2017)
                    Share2017list.append(Share2017)

                elif df3.iloc[i]['tag'].lower() == 'depreciationdepletionandamortization':

                    flagdep = flagdep + 1
                    if flagdep == 1:
                        Dep2017 = df3.iloc[i]['value']
                        if Dep2017 == '':
                            Dep2017= 0
                        Dep2017= float(Dep2017)
                        Dep2017list.append(Dep2017)

                elif df3.iloc[i]['tag'].lower() == 'interestexpense':

                    flagII = flagII + 1
                    if flagII == 1:             #interest expense tag
                        IntExp2017 = df3.iloc[i]['value']
                        if IntExp2017 == '':
                         IntExp2017= 0
                        IntExp2017= float(IntExp2017)
                        II2017list.append(IntExp2017)
                i = i + 1
            else:
                if df3.iloc[i]['ddate'].startswith('2016'):
                    if df3.iloc[i]['tag'].lower() == 'netincomeloss' or df3.iloc[index]['tag'].lower() == 'profitloss':
                        if df3.iloc[i]['qtrs'] == '3':
                            flagNI2016 = flagNI2016 + 1
                            if flagNI2016 == 1:
                                NetIncome2016 = df3.iloc[i]['value']
                                if NetIncome2016 == '':
                                    NetIncome2016 = 0
                                NetIncome2016 = float(NetIncome2016)
                                # cname = df3.iloc[index]['name']
                                # CompanyNameList.append(cname)
                                netincome2016list.append(NetIncome2016)


                    elif df3.iloc[i]['tag'].lower() == 'assets':
                            flagassets2016 = flagassets2016 + 1  # NetIncome = profitloss,netincomeloss
                            if flagassets2016 == 1:
                                Assets2016 = df3.iloc[i]['value']
                                if Assets2016 == '':
                                    Assets2016 = 0
                                Assets2016 = float(Assets2016)
                                assets2016list.append(Assets2016)



                    elif df3.iloc[i]['tag'].lower() == 'liabilities':
                        Liabilities2016 = df3.iloc[i]['value']
                        flagliabilities2016 = flagliabilities2016 + 1
                        if flagliabilities2016 == 1:
                            if Liabilities2016 == '':
                                Liabilities2016 = 0
                            Liabilities2016 = float(Liabilities2016)
                            liabilities2016list.append(Liabilities2016)
                        # if else to access tag values
                    elif df3.iloc[i]['tag'].lower() == 'assetscurrent':
                        flagCA2016 = flagCA2016 + 1
                        if flagCA2016 == 1:
                            CurrentAssets2016 = df3.iloc[i]['value']
                            if CurrentAssets2016 == '':
                                CurrentAssets2016 = 0
                            CurrentAssets2016 = float(CurrentAssets2016)
                            CA2016list.append(CurrentAssets2016)

                    elif df3.iloc[i]['tag'].lower() == 'liabilitiescurrent':

                        flagCL2016 = flagCL2016 + 1
                        if flagCL2016 == 1:
                            CurrentLiabilities2016 = df3.iloc[i]['value']
                            if CurrentLiabilities2016 == '':
                                CurrentLiabilities2016 = 0
                            CurrentLiabilities2016 = float(CurrentLiabilities2016)
                            CL2016list.append(CurrentLiabilities2016)

                    elif df3.iloc[i]['tag'].lower() == 'commonstockdividendspersharedeclared':
                        Share2016 = df3.iloc[i]['value']
                        if Share2016 == '':
                            Share2016 = 0
                        Share2016 = float(Share2016)

                    # elif df3.iloc[i]['tag'].lower() == 'salesrevenueservicesnet' or df3.iloc[i]['tag'].lower() == 'refiningandmarketingrevenue' or df3.iloc[i]['tag'].lower() == 'oilandgasrevenue' or df3.iloc[i]['tag'].lower() == 'naturalgasmidstreamrevenue' or df3.iloc[i]['tag'].lower() == 'oilandgasrevenue' or df3.iloc[i][ 'tag'].lower() == 'regulatedandunregulatedoperatingrevenue' or df3.iloc['tag'].lower() == 'interestanddividendincomeoperating' or df3.iloc[i]['tag'].lower() == 'noninterestincome' or df3.iloc[i]['tag'].lower() == 'financingrevenueandnotherinterestincomenet' or df3.iloc[i][ 'tag'].lower() == 'realestaterevenuenet' or df3.iloc[i]['tag'].lower() == 'healthcareorganizationrevenuenetofpatientservicerevenueprovisions':
                    #
                    #     flagsales2016 = flagsales2016 + 1  # NetIncome = profitloss,netincomeloss
                    #     if flagsales2016 == 1:
                    #         Sales2016 = df3.iloc[i]['value']
                    #         if Sales2016 == '':
                    #             Sales2016 = 0
                    #         Sales2016 = float(Sales2016)
                    #         Sales2016list.append(Sales2016)
                    #

                i = i + 1
        else:

            flagNI2017 = 0
            flagNI2016 = 0
            flagassets2017 = 0
            flagassets2016 = 0

            flagliabilities2016 = 0
            flagliabilities2017 = 0

            flagCA2017 = 0
            flagCL2017 = 0

            flagCA2016 = 0
            flagCL2016 = 0

            flagdep = 0
            flagII = 0
            flagsales2017 = 0
            flagsales2016 = 0
           # fq = fq.append(pd.DataFrame({'CompanyName': cname, 'NetIncome2017': NetIncome2017}, index=[0]), ignore_index=True)
            # f.iloc[fi]['CompanyName'].append(cname)
            # f.iloc[fi]['NetIncome'].append(NetIncome2017)
            # f.iloc[fi]['RetainedEarnings'].append(NetIncome2017 - Share2017)


            i = i + 1
        if index == 22500: # mock index to test code easily and with fewer iterations
            l = len(CompanyNameList)
            NetCapSpendingList = [x1 - x2 for (x1, x2) in zip(assets2017list, assets2016list)]
            NetCapSpendingList = [x1 + x2 for (x1, x2) in zip(NetCapSpendingList, Dep2017list)]

            Incomelist = [x1 - x2 for (x1, x2) in zip(netincomelist, netincome2016list)]

            ChangeinNWC = [x1 - x2 for (x1, x2) in zip(CA2017list, CL2017list)]
            ChangeinNWC1 = [x1 - x2 for (x1, x2) in zip(CA2016list, CL2016list)] #finding the ratios analysis
            FinalChangeinNWC = [x1 - x2 for (x1, x2) in zip(ChangeinNWC, ChangeinNWC1)]

            Cashflowtocreditors = [x1 - x2 for (x1, x2) in zip(liabilities2017list, liabilities2016list)]
            Cashflowtocreditorsfinal = [x1 - x2 for (x1, x2) in zip(II2017list, Cashflowtocreditors)]
            incomeincreaseordecrease = 0
            for i in Incomelist:
                if i>=0:
                    incomeincreaseordecrease = incomeincreaseordecrease + 1


            a = NetCapSpendingList
            print(len(netincomelist))
            print(len(CA2017list))
            print(len(CL2017list))
            print(len(assets2017list))

            d = pd.DataFrame({'Company':CompanyNameList,'NetIncome-2017': netincomelist})
            d1 = pd.DataFrame({'NetCapSpending': NetCapSpendingList})
            writer = pd.ExcelWriter('output.xlsx')
            d.to_excel(writer, 'Sheet1')

            d1.to_excel(writer, 'Sheet2')

            d3 = pd.DataFrame({'ChangeinNWC': FinalChangeinNWC}) #uploading to excel

            d3.to_excel(writer, 'Sheet3')

            d4 = pd.DataFrame({'CashFlowtoCreditors': Cashflowtocreditors})

            d4.to_excel(writer, 'Sheet4')
            ilist = []
            ilist.append((incomeincreaseordecrease/len(Incomelist))*100)
            d5 = pd.DataFrame({'Numbers experiencing increase in income':ilist})
            d5.to_excel(writer, 'Sheet5')





            writer.save()
            exit(0)

incomeincreaseordecrease = 0
netincomelist = []
CompanyNameList = []
Share2017list = []
netincome2017 =0
resultnum =[]
resultsub = []
finaldf =  pd.DataFrame(columns=['CompanyName','NetIncome','RetainedEarnings'])
NetIncome2017 = 0
Assets2017 = 0
Liabilities2017 = 0
CurrentAssets2017 = 0
CurrentLiabilities2017 = 0
Share2017 = 0
Dep2017 = 0
IntExp2017 = 0
Sales2016 = 0
netincome2016list = []
NetIncome2016 = 0
Assets2016 = 0
Liabilities2016 = 0
CurrentAssets2016 = 0
CurrentLiabilities2016 = 0
Share2016 = 0
Sales2017 = 0
##################creating lists to store values
assets2017list = []
liabilities2017list = []
CA2017list = []
CL2017list = []
Dep2017list = []
II2017list = []
Sales2017list = []
Sales2016list = []
assets2016list = []
liabilities2016list = []
CA2016list = []
CL2016list = []
Dep2016list = []
II2016list = []
merged = {}
######################the following are ratio analysis
NetCapSpendingList = []
url = 'https://www.sec.gov/files/dera/data/financial-statement-data-sets/2017q4.zip'  #URL to download the code from
f = urlopen(url)
print ("downloading from SEC website ")
data = f.read()
with open("SECdata.zip", "wb") as code:
    code.write(data)
SECfiles = zipfile.ZipFile('SECdata.zip')  #saving as SECdata.zip
SECfiles.extractall()
converttoCSV()
#joinCSV()
converttodict()
#mergedict()
print("Out finally")


def usedict():
    filename = "sub.txt"
    subfile = open(filename, 'r')
    resultsub = [line.split('\t') for line in subfile.readlines()]
    filename = "num.txt"
    numfile = open(filename, 'r')
    resultnum = [line.split('\t') for line in subfile.readlines()]

    i = iter(resultsub)
    dictsub = dict(zip(i, i))
    print(dictsub)

    i = iter(resultnum)
    dictnum = dict(izip(i, i))

def mergedict(new_data,new_data1):
    ds = [new_data,new_data1]

    for k in new_data:
        merged[k] = tuple(merged[k] for merged in ds)
    print("Just like that")

index = i =0
fi = 0
netincome2017 =0
d = {}
resultnum =[]
resultsub = []
finaldf =  pd.DataFrame(columns=['CompanyName','NetIncome','RetainedEarnings'])
NetIncome2017 = 0
Assets2017 = 0
Liabilities2017 = 0
CurrentAssets2017 = 0
CurrentLiabilities2017 = 0
Share2017 = 0
Dep2017 = 0
IntExp2017 = 0

merged = {}

url = 'https://www.sec.gov/files/dera/data/financial-statement-data-sets/2017q4.zip'  #URL to download the code from
f = urlopen(url)
print ("downloading from SEC website ")
data = f.read()
with open("SECdata.zip", "wb") as code:
    code.write(data)
SECfiles = zipfile.ZipFile('SECdata.zip')  #saving as SECdata.zip
SECfiles.extractall() 
converttoCSV()
#joinCSV()
converttodict()
#mergedict()
print("Out finally")
