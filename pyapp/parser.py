dataFile = open(".config/html.dat","r") # Fayli oxuma modunda ac

data = dataFile.read()                  # Fayli oxu
if(not data):
    raise ("Fayl bosdur!")

sepData = []                            # Parcala ve indexle

for i in data.split("$%"):              # Ayiriciya gore sirala
    sepData.append(i)                   # parcala ve ayiriciya yukle

def getHtmlData(index):                 # Indexe gore cagir
    global sepData                      # global deyisken olaraq ayarla
    return sepData[index]               # Verilen indexe gore getir
