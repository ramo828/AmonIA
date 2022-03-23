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

def setPrefix(_prefix):
    global categoryKey
    if(_prefix == 55):
        categoryKey = "sadə";                                   # Sade Nomreleri
    else:
        categoryKey = "sadə099";                                   # Sade Nomreleri
    global prefix
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


def loadTotal():
    totalNumb = 0
    try:
        r = conBakcell(0)
        totalJSON = json.loads(r.text);
        for tData in totalJSON:
            totalNumb = int((tData["totalElements"]))
        return totalNumb
    except TypeError:
        print("Key xətalıdır!")


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