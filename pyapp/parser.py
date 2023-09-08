import csv
import random
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

def CSV_writer(w):
    global csv_out
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

def writeCSV(_name,_pref,_data):
    global csv_out
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



prefixler = ["+99455", "+99499", "+99450", "+99451", "+99410", "+99470", "+99477"]


def alphabetical_order(counter:int):
    alph_name = ""
    if(counter <= 10):
        alph_name = "_A{0}".format(counter)
    elif(counter > 10 and counter <= 100):
        alph_name = "_B{0}".format(counter)
    elif(counter > 100 and counter <= 1000):
        alph_name = "_C{0}".format(counter)
    elif(counter > 1000 and counter <= 10000):
        alph_name = "_D{0}".format(counter)
    else:
        alph_name = "_E{0}".format(counter)
    return alph_name



counter = 0

def generate_vcf_with_prefix(number):
    name = "Metros"
    global counter
    vcf_list = []
    for prefix in prefixler:
        full_number = f"{prefix}{number}"
        vcf = f"BEGIN:VCARD\nVERSION:2.1\nN:{name}{alphabetical_order(counter)};;;\nTEL:{full_number}\nEND:VCARD"
        vcf_list.append(vcf)
        counter+=1
    return vcf_list

