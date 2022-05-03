import lib
from tqdm import tqdm
import sys

if(sys.argv[1] == "html"):
    text = False
    banner = False
elif(sys.argv[1] == "html1"):
    text = False
    banner = True
elif(sys.argv[1] == "txt"):
    text = True
else:
    text = True

allNumb = ""
allNumbText = ""
nData = ""
fileName = [
    'output/numbersOUT.txt',
    'output/numbersOUT.html',
]
fileNameIndex = 0
step = 1
endstep = 3
loadStep = 0
categoryValue = 0
htmlNumb = 1                             # sira nomresi baslama

def load(_number, prefix,category):
    global allNumb
    lib.setPrefix(prefix,category)
    if(len(_number) == 7):
        allNumb=lib.loadData(0,_number)
        lib.green()
        print(_number)
    else:
        pass

try:
    r = open("input/numbersIN.txt","r",encoding="UTF-8")
    nData = r.read()
except FileNotFoundError:
    lib.red()
    print("Fayl Tapilmadi")
if(text):
    fileNameIndex = 0
else:
    fileNameIndex = 1

w = open(fileName[fileNameIndex],"w",encoding="UTF-8")

def dataSplit(data):
    data0 = ""
    for i in data.splitlines():
        data0 +="\n"+i[0:3]+" "+i[3:5]+" "+i[5:7]
    return data0


def counter(data):
    ccl = []
    for i in data.split("\n"):
        ccl.append(i)
    
    return len(ccl)



for numb in tqdm(nData.splitlines()):          # Fayldaki melumatlari oxu
    if(numb.find("[") != -1):                  # Eger [ varsa
        if(numb.find("|") != -1):              # Eger | varsa
            step=3                             # Eger | varsa 3 addim ireli get
            endstep=5                          # ve son addimi 5'e ayarla
            loadStep=2                         # Nomre datasinin son deyerini 2 addim artir
            categoryValue = int(numb[1:2])     # Kategori deyeri
        else:
            step=1                             # deyilse addimi 1'e ayarla
            endstep=3                          # son addimi 3 et 
            loadStep=0                         # son deyeri 0 olaraq artir(deyisdirme)
        pref = int(numb[step:endstep])         # prefix deyerini al
        load(numb[endstep:10+loadStep],
        pref,categoryValue)

        for splData in tqdm(allNumb):
            if(len(splData) < 7):
                pass
            else:
                if(text):
                    allNumbText+="\n"+splData
                else:
                    if(banner):
                        lib.setBanner(dataSplit(splData[2:]),lib.prefDigit(pref),categoryValue)
                    else:
                        lib.setData(htmlNumb,dataSplit(splData[2:]),lib.prefDigit(pref),categoryValue)

            htmlNumb+=1                                               # Nomre siralamasi

    else:
        htmlNumb = 1
        load(numb,"55",0)
        for splData in tqdm(allNumb):
            if(len(splData) < 7):
                pass
            else:
                if(text):
                    allNumbText+="\n"+splData
                else:
                    if(banner):
                        lib.setBanner(dataSplit(splData[2:]),lib.prefDigit(pref),categoryValue)
                    else:
                        lib.setData(htmlNumb,dataSplit(splData[2:]),lib.prefDigit(pref),categoryValue)

            htmlNumb+=1                                              # Nomre siralamasi

print("\nÜmumi nömrə sayı: "+str(htmlNumb))
print("\nFaylın adresi: "+fileName[fileNameIndex])

if(text):
    w.write(allNumbText)
else:
    if(banner):
        w.write(lib.toHTML1())
    else:
        w.write(lib.toHTML())