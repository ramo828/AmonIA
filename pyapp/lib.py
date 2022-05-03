import os.path                 # Lib
import os
import time as tm
from typing import Type
import requests
import subprocess
import json
import parser as ps
from colorama import Fore, Back, Style

bKey ="Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJNQUlOIiwiZXhwIjoxNjUzMDAyODQ1fQ.zA2ibHv4fGfNlP_3AlcaGZ6ROuLLBBSLasYXlqna87YktQNXgY4XzYf5lTqLc-42YKbZse4alB3fwAE3ZuTAJw"
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




cat055 = [
            "Sadə",
            "Xüsusi1",
            "Xüsusi2",
        ]

cat099 = [
            "Sadə",
            "Bürünc",
            "Gümüş",
            "Qızıl",
            "Platin",
            ]

cat = ""


pref = [
            "055",
            "099",
]

cost055 = [
            "15",
            "85",
            "135",
    ]

cost099 = [
            "15",
            "140",
            "250",
            "750",
            "2500",
    ]
prefG = ""
cost = ""
data = ""

def prefDigit(_data):
    if(_data == 55):
        return 0
    elif(_data == 99):
        return 1

def setData(no,_data, prefID,catID):
    global data
    global cat
    global cost
    global prefG
    if(prefID == 0):
        prefG = pref[prefID]
        cat = cat055[catID]
        cost = cost055[catID]
    elif(prefID == 1):
        prefG = pref[prefID]
        cat = cat099[catID]
        cost = cost099[catID]
    data +="""
    <tr>\n
            <td>{0}</td>
            <td>{1}</td>
            <td>{2} {3}</td>
            <td>{4}</td>
    </tr>
    """.format(no,cat,prefG,_data,cost)

def setBanner(_data, prefID,catID):
    global data
    global cost
    tag = ""
    if(prefID == 0):
        prefG = pref[prefID]
        cost = cost055[catID]
    elif(prefID == 1):
        prefG = pref[prefID]
        cost = cost099[catID]
    if(int(cost) > 999):
        tag = "h4"
    elif(int(cost) > 99):
        tag = "h3"
    else:
        tag = "h2"
    data += """
<body>
  <div class="image">
    <img src="../img/77.jpg" alt="" height=550/>
     <h1>{0} {1}</h1>
     <{3}>{2}</{3}>
  </div>
  <hr>
    """.format(prefG,_data,cost,tag)


def toHTML():
    dat1 = ps.getHtmlData(0)+ps.getHtmlData(1)+data+ps.getHtmlData(2)+ps.getHtmlData(3)+ps.getHtmlData(4)
    return dat1

def toHTML1():
    dat1 = ps.getHtmlData(0)+data+ps.getHtmlData(2)+ps.getHtmlData(4)
    return dat1

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
    dataFour = []
    dataTwo = ""
    data = json.loads(r.text);
    for i in data:
        dataTwo = (i["freeMsisdnList"])
    for i2 in dataTwo:
        dataFour.append(str(i2["msisdn"]))
    return dataFour

def vcardWrite(w,contactName,prefix,pre,dataFour,count1):
    w.write(
    dataVcard[0]
	+dataVcard[1]+contactName+conv_numeric(count1)+"\n"	
	+dataVcard[2]+contactName+conv_numeric(count1)+"\n"
	+dataVcard[3]+prefix[pre]+dataFour[0:7]+"\n"
	+dataVcard[4]
	+dataVcard[5])
