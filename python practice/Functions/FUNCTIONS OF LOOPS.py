def printnum():
    for i in range(1,11):
        print(i)
    return i

def printnumrev():
    for i in range(10,0,-1):
        print(i)
    return i

def fibonacci(n):
    x=0
    y=1
    c=1
    for c in range(n):
        print(x)
        z=x+y
        x=y
        y=z
    return z

def factorial(n):
    f=1
    c=1
    for c in range(1,n+1):
        f=f*c
    return f

def add(n):
    i=1
    sm=0
    for i in range(1,i+1):
        sm=sm+i
    return sm

def table(t):
    for n in range(1,11,+1):
        print(f"{t}x{n}={t*n}")
    return t

def leapy():
    year=[]
    for i in range(1900,2030):
        if(i%400==0)or (i%4==0 and i%100!=0):
            year.append(i)
    return year

def even():
    data=[]
    for i in range(1,101):
        if(i%2==0):
            data.append(i)
    return data

def reverse(n):
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev

def palindrome(n):
    rev=0
    n1=n
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if(n1==rev):
        print("palindrome no")
    else:
        print("not palindrome no")

def strong(n):
    n1=n
    sm=0
    while(n!=0):
        rem=n%10
        f=1
        for i in range(1,rem+1):
            f=f*i
        sm=sm+f
        n=n//10
    if(n1==sm):
        print("strong number")
    else:
        print("not strong number")


def armstrong(n):
     n1=n
     n2=n
     sm=0
     c=0
     while(n!=0):
         n=n//10
         c=c+1
     while(n1!=0):
         rem=n1%10
         sm=sm+rem**c
         n1=n1//10
     if(n2==sm):
         print("armstrong number")
     else:
         print("not armstrong number")

         
def neon(n):
    sq=n**2
    sm=0
    while(sq!=0):
        rem=sq%10
        sm=sm+rem
        sq=sq//10
    if(n==sm):
        print("neon number")
    else:
        print("not neon number")

        
        

    
    
    
        
    
    
    

    
