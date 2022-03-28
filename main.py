import subprocess

print("\t----------------\n\t[---RamoSOFT---]\n\t----------------\n")
print("\t---AMONIA---")
choise = int(input("\n\t1 - Numerator\n\t----------\n\t2 - Auto Serializer\n\t----------\n\t0 - Exit\n>> "))
if(choise == 1):
    subprocess.call(["python", "pyapp/aserial.py"])
elif(choise == 2):
    subprocess.call(["python", "pyapp/numerator.py"])
elif(choise == 0):
    exit(1)
else:
    raise TypeError("Xətalı Əmr!")
