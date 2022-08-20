import lib
from tqdm import tqdm
import sys
import csv
import json
import os

if(sys.argv[1] == "html"):
    text = False
    banner = False
    csv_bool = False
elif(sys.argv[1] == "html1"):
    text = False
    csv_bool = False
    banner = True
elif(sys.argv[1] == "csv"):
    text = False
    banner = False
    csv_bool = True
elif(sys.argv[1] == "txt"):
    text = True
    banner = False
    csv_bool = False
else:
    text = True
    banner = False
    csv_bool = False

allNumb = ""
allNumbText = ""
nData = ""
fileName = [
    'output/numbersOUT.txt',
    'output/numbersOUT.html',
    'output/numbersOUT.csv',

]
fileNameIndex = 0
step = 1
endstep = 3
loadStep = 0
categoryValue = 0
htmlNumb = 1                             # sira nomresi baslama



def load(_number, prefix,category):
    global allNumb
    loadCounter = 0
    lib.setPrefix(prefix,category)
    if(len(_number) == 7):
        while(True):
            if(not lib.loadData(loadCounter,_number)):
                break
            if(loadCounter != 0):
                allNumb.extend(lib.loadData(loadCounter,_number))
            else:
                allNumb=lib.loadData(0,_number)
            allNumb=lib.loadData(loadCounter,_number)
            lib.green()
            print("Səhifə sayı: "+str(loadCounter+1))
            loadCounter+=1
        print(_number)
    else:
        pass

def loadNar(_number, _prefix, category):
    loadCounter = 0
    if(_prefix == "70"):
        prefix = 0
    elif(_prefix == "77"):
        prefix = 1
    global allNumb
    lib.setNarPrefix(prefix)
    lib.setNarCategory(category)
    lib.inputNumber(_number)
    if(len(_number) == 7):
        while(True):
            if(not lib.loadNarData(loadCounter)):
                break
            if(loadCounter != 0):
                allNumb.extend(lib.loadNarData(loadCounter))
            else:
                allNumb=lib.loadNarData(0)
            lib.green()
            print("Səhifə sayı: "+str(loadCounter+1))
            loadCounter+=1
        print(_number)
    else:
        pass

try:
    r = open("input/input.json","r")
    nData = json.load(r)
except FileNotFoundError:
    lib.red()
    print("Fayl Tapilmadi")
if(text):
    fileNameIndex = 0
elif(csv_bool):
    fileNameIndex = 2
else:
    fileNameIndex = 1

w = open(fileName[fileNameIndex],"w",encoding="UTF-8")

def dataSplit(data):
    data0 = ""
    for i in data.splitlines():
        if(len(i) == 7):
            data0 +="\n"+i[:3]+" "+i[3:5]+" "+i[5:7]
        elif(len(i) == 9):
            data0 +="\n"+i[:2]+" "+i[2:5]+" "+i[5:7]+" "+i[7:9]
    return data0

if(csv_bool):
    csv_out = csv.writer(w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_out.writerow(['Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name',
       'Given Name Yomi', 'Additional Name Yomi', 'Family Name Yomi',
       'Name Prefix', 'Name Suffix', 'Initials', 'Nickname', 'Short Name',
       'Maiden Name', 'Birthday', 'Gender', 'Location', 'Billing Information',
       'Directory Server', 'Mileage', 'Occupation', 'Hobby', 'Sensitivity',
       'Priority', 'Subject', 'Notes', 'Language', 'Photo', 'Group Membership',
       'Phone 1 - Type', 'Phone 1 - Value', 'Phone 2 - Type',
       'Phone 2 - Value', 'Organization 1 - Type', 'Organization 1 - Name',
       'Organization 1 - Yomi Name', 'Organization 1 - Title',
       'Organization 1 - Department', 'Organization 1 - Symbol',
       'Organization 1 - Location', 'Organization 1 - Job Description'])
else:
    pass

def writeCSV(_name,_pref,_data):

    csv_out.writerow([
    _name, #0
    _name, #1
    '',    #2
    '',    #3
    '',    #4
    '',    #5
    '',    #6
    '',    #7
    '',    #8
    '',    #9
    '',    #10
    '',    #11
    '',    #12
    '',    #13
    '',    #14
    '',    #15
    '',    #16
    '',    #17
    '',    #18
    '',    #19
    '',    #20
    '',    #21
    '',    #22
    '',    #23
    '',    #24
    '',    #25
    '',    #26
    '',    #27
    '* myContacts',    #28
    'Mobile',          #29
    _pref+_data,       #30
    '',    #31
    '',    #32
    '',    #33
    '',    #34
    '',    #35
    '',    #36
    '',    #37
    '',    #38
    '',    #39
    '',    #40
    ])

def counter(data):
    ccl = []
    for i in data.split("\n"):
        ccl.append(i)
    
    return len(ccl)

latestData = nData["numbers"]

for numb in tqdm(latestData):          # Fayldaki melumatlari oxu
    pref = numb["prefix"]
    categoryValue = numb["category"]
    number = numb["number"]
    if(pref == "70" or pref == "77"):
        print("---NAR---")
        loadNar(number, pref, categoryValue)
    else:
        print("---BAKCELL---")
        load(number,pref,categoryValue)
    prefN = lib.getConvData(lib.prefDigit(pref),categoryValue,0)
    for splData in tqdm(allNumb):
        if(len(splData) < 7):
            pass
        else:
            if(text):
                allNumbText+="\n"+splData
            else:
                if(banner):
                    lib.setBanner(dataSplit(splData[2:]),lib.prefDigit(pref),categoryValue)
                elif(csv_bool):
                    writeCSV("Metros "+str(htmlNumb),prefN,splData[2:])
                else:
                    lib.setData(htmlNumb,dataSplit(splData[2:]),lib.prefDigit(pref),categoryValue)

        htmlNumb+=1                                               # Nomre siralamasi



print("\nÜmumi nömrə sayı: "+str(htmlNumb))
print("\nFaylın adresi: "+fileName[fileNameIndex])
if(text):
    w.write(dataSplit(allNumbText))
else:
    if(banner):
        w.write(lib.toHTML1())
    elif(csv_bool):
        pass
    else:
        w.write(lib.toHTML())
