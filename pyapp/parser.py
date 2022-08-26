import csv
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