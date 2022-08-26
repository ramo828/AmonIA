import os.path                 # Lib
import os
import time as tm
from typing import Type
import requests
import subprocess
import json
import parser as ps
from colorama import Fore, Back, Style

key = [
    # Bakcell
    "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJNQUlOIiwiZXhwIjoxNjYyNjM2OTI1fQ.sqL5xgOiU1rmrAVBzm4xH7B9GrMYqqed-fda7pn7IlyrtMKUfSWnvBwaA-12-3fT8uLwBrUel9iSMpGQ-C6Gqw",
    # Nar
    "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI4MjQtMDAzOCIsImF1dGgiOiJQUkVQQUlES0lULFdUVFgsSVNQLERVUExJQ0FURSxSRUFDVElWQVRJT04sRFVQTElDQVRFX0ZVTExfQVVUT01BVElPTixSRVNUT1JBVElPTl9TQyxSRUFDVElWQVRJT05fRlVMTF9BVVRPTUFUSU9OLERBVEFfQlVORExFLFRQX0NIQU5HRSxSRUNIQVJHRV9MT0ciLCJleHAiOjE2NjE2MTAwMjZ9.xhdokVP8Ce3lUwC7qZ1SR-oETsC7ZWZ4EyzG3J-yCKnbapIvKzfveG62zrwgIlVG7-xqDMnvcn6AM_vw-i8tpQ",
]

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

prestigeData = [
    "",                  # Simple
    "GENERAL",                         # All
    "PRESTIGE",
    "PRESTIGE1",
    "PRESTIGE2",
    "PRESTIGE3",
    "PRESTIGE4",
    "PRESTIGE5",
    "PRESTIGE6",
    "PRESTIGE7",
]
sizeNar = 2000


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

def getConvData(prefID,catID,setData):
    global cat
    global prefG
    if(prefID == 0):
        prefG = pref[prefID]
        cat = cat099[catID]
    elif(prefID == 1):
        prefG = pref[prefID]
        cat = cat099[catID]
    if(setData == 0):
        return prefG
    else:
        return cat


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


url = dict()                                               # URL lugeti
url["Bakcell"] = "https://public-api.azerconnect.az/msbkcposappreservation/api/freemsisdn-nomre/search"
url["Nar"] = "https://public-api.azerconnect.az/msazfposapptrans/api/msisdn-search" 

prefixNarData = ["70", "77"]


def setHeader(opCode):
    headers = {'content-type': 'application/json',         # Content type json
    'Accept':'application/json, text/plain, */*',          # Accept type json
    'Accept-Encoding':'gzip, deflate, br',                 # Encoding gzip compressed data
    'Accept-Language':'tr-TR,tr;q=0.9,az-TR;q=0.8,az;q=0.7,en-US;q=0.6,en;q=0.5',
     'Authorization': key[opCode],
    'Connection':'keep-alive'}
    return headers

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
    if(_prefix == "55"):
        if(category == "0"):
            categoryKey = "sadə";                                         # Sade Nomreleri
        elif(category == "1"):
            categoryKey = "xüsusi2";                                      # Xususi 1 Nomreleri
        elif(category == "2"):
            categoryKey = "xüsusi1";                                      # Xususi 2 Nomreleri
        else:
            raise TypeError("Xətalı seçim!")
    elif(_prefix == "99"):
        if(category == "0"):
            categoryKey = "sadə099";                                    # Sade Nomreleri
        elif(category == "1"):
            categoryKey = "bürünc";                                     # buruc Nomreleri
        elif(category == "2"):
            categoryKey = "gümüş";                                      # Gumus Nomreleri
        elif(category == "3"):
            categoryKey = "qızıl";                                      # Qizil Nomreleri
        elif(category == "4"):
            categoryKey = "platin";                                     # Platin Nomreleri
        else:
            raise TypeError("Xətalı seçim!")

    prefix = _prefix


def conBakcell(page, number):
    r = requests.get(url['Bakcell'], params={"prefix":prefix,
    "msisdn":number,                                        # Nomre datasi
    "categoryId":category[categoryKey],                     # Kategorya
    "showReserved":"true",                                  # Sifaris verilenler
    "size":"2000",                                          # Maksimum nomre sayi
    "page":page},                                           # Maksimum sehife sayi
    headers=setHeader(0))                                   # Header
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

def loadTotal(number):
    totalNumb = 0
    try:
        r = conBakcell(0,number)
        totalJSON = json.loads(r.text)
        for tData in totalJSON:
            totalNumb = int((tData["totalElements"]))
        return totalNumb
    except TypeError:
        red()
        print("Key xətalıdır!")

def vcardWrite(w,contactName,prefix,pre,dataFour,count1):
    w.write(
    dataVcard[0]
	+dataVcard[1]+contactName+conv_numeric(count1)+"\n"	
	+dataVcard[2]+contactName+conv_numeric(count1)+"\n"
	+dataVcard[3]+prefix[pre]+dataFour[0:7]+"\n"
	+dataVcard[4]
	+dataVcard[5])


# Nar 


def setNarCategory(prestige_):
    global prestige
    prestige = prestigeData[int(prestige_)]


def inputNumber(_number):
    global number
    number = _number


def setNarPrefix(prefixNar_):
    global prefixNar
    prefixNar = prefixNarData[int(prefixNar_)]

def narParams(page):                                      # Local Function
    num = [
    number[0],                                            # Split part1                                  
    number[1],number[2],                                  # Split part2 
    number[3],number[4],                                  # Split part3
    number[5],number[6]]                                  # Split part4
    params = {"prefix":prefixNar,
        "a1":num[0].replace("x", ""),
        "a2":num[1].replace("x", ""),
        "a3":num[2].replace("x", ""),
        "a4":num[3].replace("x", ""),
        "a5":num[4].replace("x", ""),
        "a6":num[5].replace("x", ""),
        "a7":num[6].replace("x", ""),
        "prestigeLevel":prestige,
        "size":sizeNar,
        "page":page }
    return params

def setHeader(opCode):
    headers = {'content-type': 'application/json',         # Content type json
    'Accept':'application/json, text/plain, */*',          # Accept type json
    'Accept-Encoding':'gzip, deflate, br',                 # Encoding gzip compressed data
    'Accept-Language':'tr-TR,tr;q=0.9,az-TR;q=0.8,az;q=0.7,en-US;q=0.6,en;q=0.5',
     'Authorization': key[opCode],
    'Connection':'keep-alive'}
    return headers


def conNar(page):
    try:
        params = narParams(page)
        r = requests.get(url["Nar"],params=params,headers=setHeader(1), timeout=60)
    except requests.ConnectionError as e:
        print("İnternet bağlantınızda problem var! İnterneti yoxlayıb yenidən cəhd edin\n")
        print(str(e))            
    except requests.Timeout as e:
        print("Zaman aşımı! Məlumatlar serverdən alına bilmir!")
        print(str(e))
    except requests.RequestException as e:
        print("Ümumi xəta")
        print(str(e))
    except KeyboardInterrupt:
        print("Program dəyandırıldı")
    return r
    


def loadNarData(page):
    narNumber = []
    narCounter = 0
    narTwo = ""
    r = conNar(page)
    if(len(r.text) > 7):
        narData = json.loads(r.text)
    elif(r.status_code != 200):
        print("Key xətalıdır")
        exit(1)
    else:
        return ""
    for nar in narData:
        narTwo = (nar["msisdn"])
        narNumber.append(str(narTwo[3:]))
        narCounter=narCounter+1
    return narNumber
 
def narPageCount():
    meData = ""
    page = 0
    while True:
        os.system("clear")
        print("Böyük həcmli datalarda yüklənmə zaman ala bilər!\n")
        print("Səhifə: {0}\n".format(page))
        meData=loadNarData(page)
        if(not meData):
            break
        else:
            page+=1
    return page

def loadNarTotal(page):
    totalNumb = 0
    numberNar = []
    try:
        r = conNar(page)
        totalJSON = json.loads(r.text)
        for tData in totalJSON:
            totalNumb = (tData["msisdn"])
            numberNar.append(totalNumb)
        return len(numberNar)
    except TypeError:
        print("Key xətalıdır!")