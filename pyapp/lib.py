import os.path                 # Lib
import os
import time as tm
from typing import Type
import requests
import subprocess
import json
from colorama import Fore, Back, Style

bKey ="Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJNQUlOIiwiZXhwIjoxNjUxMTYzMjQxfQ.nSGnhZ5Q88X7ff77PkHCWAlBEJJfzks19-gMOG4Wu9M1Pz_qvlTnFEB4iMFLXt6xoDRpGKJuNj2iMdmZju1S3Q"
category = dict()
categoryKey = "sadə";                                      # Sade Nomreleri
category["sadə"] = "1429263300716842758";                  # Sade key
category["xüsusi1"] = "1579692503636523114";               # Xususi1 key
category["xüsusi2"] = "1579692547752973099";               # Xususi2 key
categoryKey055 = "sadə"                                    # 099 sade nomreler
#------------------099----------------------------
category["sadə099"] = "1574940031138475856";               # Sade key
category["bürünc"] = "1582551518546595643";                # Burunc key
category["gümüş"] = "1582551485948558941";                 # Gumus key
category["qızıl"] = "1582551461421619154";                 # Qizil key
category["platin"] = "1582551437850968791";                # Platin key
categoryKey099 = "bürünc"                                  # Buruc nomreler
prefixSel = ["55","99"]


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

defaultContactName = "Metros"
dirs = os.getcwd()+"/.config/"                           # Oldugun qovluq


def magenta():
    print(Style.RESET_ALL)
    print(Fore.MAGENTA)

def light_magenta():
    print(Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX)

def lightGreen():
    print(Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX)

def red():
    print(Style.RESET_ALL)
    print(Fore.RED) 

def light_red():
    print(Style.RESET_ALL)
    print(Fore.LIGHTRED_EX)

def yellow():
    print(Style.RESET_ALL)
    print(Fore.YELLOW)

def light_blue():
    print(Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX)

def light_black():
    print(Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX)

def green():
    print(Style.RESET_ALL)
    print(Fore.GREEN)


def detectOS():
    if(subprocess.check_output(['uname', '-o']).strip() == b'Android'):
        return True
    else:
        return False

def readContactName():
    configData = ""
    if(os.path.exists(dirs+"contact.name")):
        config = open(dirs+"contact.name","r")
        configData = config.read()
        return configData
    else:
        configData = defaultContactName
        return configData

def setPrefix(_prefix,category):
    global categoryKey
    global prefix
    if(_prefix == 55):
        if(category == 0):
            categoryKey = "sadə";                                         # Sade Nomreleri
        elif(category == 1):
            categoryKey = "xüsusi2";                                      # Xususi 1 Nomreleri
        elif(category == 2):
            categoryKey = "xüsusi1";                                      # Xususi 2 Nomreleri
        else:
            raise TypeError("Xətalı seçim!")
    elif(_prefix == 99):
        if(category == 0):
            categoryKey = "sadə099";                                    # Sade Nomreleri
        elif(category == 1):
            categoryKey = "bürünc";                                     # buruc Nomreleri
        elif(category == 2):
            categoryKey = "gümüş";                                      # Gumus Nomreleri
        elif(category == 3):
            categoryKey = "qızıl";                                      # Qizil Nomreleri
        elif(category == 4):
            categoryKey = "platin";                                     # Platin Nomreleri
        else:
            raise TypeError("Xətalı seçim!")

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

def vcardWrite(w,contactName,prefix,pre,dataFour,count1):
    w.write(
    dataVcard[0]
	+dataVcard[1]+contactName+conv_numeric(count1)+"\n"	
	+dataVcard[2]+contactName+conv_numeric(count1)+"\n"
	+dataVcard[3]+prefix[pre]+dataFour[0:7]+"\n"
	+dataVcard[4]
	+dataVcard[5])
