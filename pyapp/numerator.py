import lib
import lib_num
from tqdm import tqdm

prefixAz = ["+99450","+99451","+99410","+99499","+99470","+99477"]
prefBegin = 0
prefEnd = 5
contactName = "Metros"
split = "-"

w = open("output/contacts.vcf","w+")
w1 = open("output/contacts.txt","w+")

def makeTXT(series):
    count = 0
    dataT = lib_num.makeNumb(series)
    for tx in tqdm(dataT.split('\n')):
        w1.write(tx[0:3]+split+tx[3:5]+split+tx[5:7]+"\n")
        count=count+1
    print("\nHazırlandı: "+str(count))



def makeVCF(series):
    count = 0
    for pre in tqdm(range(prefBegin,prefEnd)):
            for n in tqdm(lib_num.makeNumb(series).split("\n")):
                dataFour = n
                lib.vcardWrite(w,                               # Vcard skelet
                contactName,                                    # Kontakt adi
                prefixAz,                                       # Prefix
                pre,                                            # Prefix Araligi
                dataFour,                                       # Yekun data
                count)                                          # Kontaktin ad ardicilligi
                count=count+1
    print("\nHazırlandı: "+str(count))
    print("\nÜmumi: "+str(count*6))

print("\n\t-----------------------\n")
series = input("Nomreni daxil edin: ")
cat = int(input("0 - TXT\n1 - VCF\n>> "))
if(cat == 0):
    makeTXT(series)
elif(cat == 1):
    makeVCF(series)
else:
    raise TypeError("Xətalı əmr")