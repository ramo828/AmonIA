import lib
from tqdm import tqdm
import sys
import json
import os
import math
import parser as ps

if(sys.argv[1] == "html"):
    text = False
    banner = False
    csv_bool = False
    vcf = False

elif(sys.argv[1] == "html1"):
    text = False
    csv_bool = False
    banner = True
    vcf = False

elif(sys.argv[1] == "csv"):
    text = False
    banner = False
    csv_bool = True
    vcf = False

elif(sys.argv[1] == "txt"):
    text = True
    banner = False
    csv_bool = False
    vcf = False

elif(sys.argv[1] == "vcf"):
    text = False
    banner = False
    csv_bool = False
    vcf = True
else:
    text = True
    banner = False
    csv_bool = False

allNumb = []
allNumbText = ""
nData = ""
fileName = [
    'output/numbersOUT.txt',
    'output/numbersOUT.html',
    'output/numbersOUT.csv',
    'output/numbersOUT.vcf',

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

    rawNumber = lib.loadTotal(_number)/2000
    number = math.ceil(rawNumber)
    if(len(_number) == 7):
        for sehifeninSayi in range(number):
            if(number > 1):
                os.system("clear")
                print("Səhifə sayı: {}".format(loadCounter+1))
            allNumb.extend(lib.loadData(loadCounter,_number))
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
            allNumb.extend(lib.loadNarData(loadCounter))
            if(lib.loadNarTotal(loadCounter) < 1):
                break
            else:    
                print("Səhifə sayı: {}".format(loadCounter+1))
                
            lib.green()
            loadCounter+=1
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
elif(vcf):
    fileNameIndex = 3
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
    ps.CSV_writer(w)
else:
    pass


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
                ps.writeCSV("Metros "+str(htmlNumb),prefN,splData[2:])
            elif(vcf):
                vcf_file =  ps.generate_vcf_with_prefix(splData[2:])
                for vcf_split in vcf_file:
                    w.write(vcf_split+"\n")
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
