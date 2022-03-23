import lib
allNumb = ""
nData = ""
def load(_number, prefix):
    global allNumb
    lib.setPrefix(prefix)
    if(len(_number) == 7):
        allNumb=allNumb+lib.loadData(0,_number)
        print(_number)

try:
    r = open("numbersIN.txt","r",encoding="UTF-8")
    nData = r.read()
except FileNotFoundError:
    print("Fayl Tapilmadi")

w = open("numbersOUT.txt","w",encoding="UTF-8")



for numb in nData.split("\n"):
    if(numb.startswith("[")):
        pref = int(numb[1:3])
        load(numb[3:10],pref)
    else:
        load(numb,"55")

w.write(allNumb.replace(" ",""))