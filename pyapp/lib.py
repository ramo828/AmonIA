import os.path                 # Lib
import os
import time as tm
import requests
import subprocess
import json

bKey ="Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJNQUlOIiwiZXhwIjoxNjQ5MzM0NzAyfQ.N2Jt28lAVMLhw4mnGJwM0QbHsEaW8c3raG-xzjufnh05uGPrJuNZvfsy8-A-M-suzpCYV-XYgBrthwui7NAadw"
category = dict()
categoryKey = "sadə";                                   # Sade Nomreleri
category["sadə"] = "1429263300716842758";               # Sade key
category["sadə099"] = "1574940031138475856";            # Sade key

url = "https://public-api.azerconnect.az/msbkcposappreservation/api/freemsisdn-nomre/search";

headers = {'content-type': 'application/json',          # Content type json
'Accept':'application/json, text/plain, */*',           # Accept type json
'Accept-Encoding':'gzip, deflate, br',                  # Encoding gzip compressed data
'Accept-Language':'tr-TR,tr;q=0.9,az-TR;q=0.8,az;q=0.7,en-US;q=0.6,en;q=0.5',
'Authorization':bKey,
'Connection':'keep-alive'}

dataVcard = [
 "BEGIN:VCARD\n"
,"N:","FN:"
,"TEL;TYPE=WORK,MSG:"
,"EMAIL;TYPE=INTERNET:\n"
,"END:VCARD\n"]


def setPrefix(_prefix):
    global categoryKey
    global prefix
    if(_prefix == 55):
        categoryKey = "sadə";                                   # Sade Nomreleri
    elif(_prefix == 99):
        categoryKey = "sadə099";                                   # Sade Nomreleri
    prefix = _prefix


def conBakcell(page, number):
    r = requests.get(url, params={"prefix":prefix,
    "msisdn":number,                                        # Nomre datasi
    "categoryId":category[categoryKey],                     # Kategorya
    "showReserved":"true",                                  # Sifaris verilenler
    "size":"2000",                                          # Maksimum nomre sayi
    "page":page},                                           # Maksimum sehife sayi
    headers=headers)                                        # Header
    return r

def conv_numeric(counter):
    sonluq = ["a","b","c","d","e","f","g"]
    clone = ""
    for i in range(counter):
        if(i<10):
            clone = "_"+sonluq[0]+str(i)
        elif(i<100):
            clone = "_"+sonluq[1]+str(i)
        elif(i<1000):
            clone = "_"+sonluq[2]+str(i)
        elif(i<10000):
            clone = "_"+sonluq[3]+str(i)
    return clone;


def loadData(page, number):
    r = conBakcell(page, number)
    dataFour = ""
    dataTwo = ""
    data = json.loads(r.text);
    for i in data:
        dataTwo = (i["freeMsisdnList"])
    for i2 in dataTwo:
        dataFour = dataFour+str(i2["msisdn"])+"\n"
    return dataFour
try:
    w = open("output/contact.vcf","w")
except FileNotFoundError:
    pass
def vcardWrite(w,contactName,prefix,pre,dataFour,count1):
    w.write(
    dataVcard[0]
	+dataVcard[1]+contactName+conv_numeric(count1)+"\n"	
	+dataVcard[2]+contactName+conv_numeric(count1)+"\n"
	+dataVcard[3]+prefix[pre]+dataFour[0:7]+"\n"
	+dataVcard[4]
	+dataVcard[5])