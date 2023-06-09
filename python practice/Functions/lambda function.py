##1. item with highest value and lowest value count
##items=[{"apple":5},{"banana":8},{"orange":7},{"grapes":4}]
##
##def maxprice():
##    d={}
##    for fruits in items:
##        d.update(fruits)
##    x=sorted(d.items(),key=lambda tup : tup[1])
##    return x[-1]
##
##def minprice():
##    d={}
##    for fruits in items:
##        d.update(fruits)
##    x=sorted(d.items(),key=lambda tup : tup[1])
##    return x[0]

##2. create a lambda function to sort the name list according to their surname.
##name = ["jay A kumar","deeplak N sharma","rohit N yadav","mithilesh singh","payal vasave","Fahad Momin"]
##
##res=sorted(name,key= lambda string:string.lower().split()[-1])
##print(res)

##3. using map function, create a lambda expression to convert the degree celcius to fahrenheit
##temp =[('kashmir',1),('mumbai',16),('chennai',18),('kerla',20)]

##formula - f=9/5xc+32

##def ctof(tup):
##    return(tup[0],(9/5)*tup[1]+32)
##res=map(ctof,temp)

##4.square of 1-10

x=[1,2,3,4,5,6,7,8,9,10]

def square(n):
    return n*n
def mymap(square,x):
    data=[]
    for n in x:
        data.append(square(n))
    return data
    
