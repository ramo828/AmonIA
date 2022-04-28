from nis import cat
import lib
from tqdm import tqdm

allNumb = ""
nData = ""


def load(_number, prefix,category):
    global allNumb
    lib.setPrefix(prefix,category)
    if(len(_number) == 7):
        allNumb=allNumb+""+lib.loadData(0,_number)
        lib.green()
        print(_number)

try:
    r = open("input/numbersIN.txt","r",encoding="UTF-8")
    nData = r.read()
except FileNotFoundError:
    lib.red()
    print("Fayl Tapilmadi")
w = open("output/numbersOUT.html","w",encoding="UTF-8")


step = 1
endstep = 3
loadStep = 0
categoryValue = 0

def dataSplit(data):
    data0 = ""
    for i in data.split("\n"):
        data0 +="\n"+i[0:3]+" "+i[3:5]+" "+i[5:7]
    return data0



for numb in tqdm(nData.split("\n")):
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
        for splData in tqdm(allNumb.split("\n")):
            if(len(splData) < 7):
                pass
            else:
                lib.setData(dataSplit(splData[2:]),lib.prefDigit(pref),categoryValue)
    else:
        load(numb,"55",0)
        for splData in tqdm(allNumb.split("\n")):
            if(len(splData) < 7):
                pass
            else:
                lib.setData(dataSplit(splData[2:]),lib.prefDigit(pref),categoryValue)

w.write(lib.toHTML())
