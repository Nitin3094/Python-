def read():
    file = open("nitindoc.txt","r")
    cont = file.read()
    print(cont)
    file.close()

def write(text):
    file = open("nitindoc.txt","w")
    cont = file.write(text)
    print(cont)
    file.close()

def append():
    file = open("nitindoc.txt","a")
    cont = file.write("my school name is shishuvihar dadar")
    print(cont)
    file.close()

def withread():
    with open("nitindoc.txt","r") as file:
        b = file.read()
        print(b)
def withwrite():
    with open("nitnidoc.txt","w") as file:
        c=file.write("i am dding one line")
        print(c)
def withappend():
    with open("nitindoc.txt","a") as file:
        d = file.write("i am adding two more lines")
        print(d)


#copy file
f1 = open("kakashi.jfif","rb")
f2 = open("copykakshi.jfif","wb")
for data in f1:
    f2.write(data)
f1.close()
f2.close()
        
    
