count = 0                                          # modulation counter


def calculate(data):
    count = 0
    for ss in data:
        if(ss == 'x'):
            count=count+1
    return count

def modulation(data):
    global count
    if(calculate(data) == count):
        count = 0
    hesabat = ""
    hesabat=hesabat+"z{0}y".format(count)
    count=count+1
    return hesabat

def say(data):
    temp = ""
    count = 0
    for ss in data:
        if(ss == 'x'):
            temp = temp+data[count].replace("x",modulation(data)).format(0).replace("z","{").replace("y","}")  # sadece x'ler
        elif(ss.isnumeric()):
            temp = temp+data[count]                                                                            # sadece nomreler
        count = count +1
    return temp

def one(data):
    _data = ""
    for i in range(10):
        _data=_data+"\n"+say(data).format(i)
    return _data

def two(data):
    _data = ""
    for i in range(10):
        for j in range(10):
            _data=_data+"\n"+say(data).format(i,j)
    return _data

def three(data):
    _data = ""
    for i in range(10):
        for j in range(10):
            for k in range(10):
                _data=_data+"\n"+say(data).format(i,j,k)
    return _data


def four(data):
    _data = ""
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for n in range(10):
                    _data=_data+"\n"+say(data).format(i,j,k,n)
    return _data

def makeNumb(data):
    sayX = calculate(data)
    if(sayX == 0):
        return data
    elif(sayX == 1):
        return one(data)
    elif(sayX == 2):
        return two(data)
    elif(sayX == 3):
        return three(data)
    elif(sayX == 4):
        return four(data)

