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

w = open("output/numbersOUT.txt","w",encoding="UTF-8")


step = 1
endstep = 3
loadStep = 0
categoryValue = 0

for numb in tqdm(nData.split("\n")):
    if(numb.find("[") != -1):
        if(numb.find("|") != -1):
            step=3
            endstep=5
            loadStep=2
            categoryValue = int(numb[1:2])
        else:
            step=1
            endstep=3
            loadStep=0
        pref = int(numb[step:endstep])
        load(numb[endstep:10+loadStep],pref,categoryValue)
    else:
        load(numb,"55",0)
w.write(allNumb.replace(" ",""))
