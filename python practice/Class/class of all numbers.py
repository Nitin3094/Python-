##class palindromeno():
##    def __init__(self):
##        pass
##    def check(self,num):
##        n1=num
##        rev=0
##        while(num!=0):
##            rem=num%10
##            rev=rev*10+rem
##            num=num//10
##
##        if(n1==rev):
##            return True
##        else:
##            return False
##        
##obj = palindromeno()
##
##num = 6543
##
##if(obj.check(num)):
##    print("palindrome")
##else:
##    print("not palindrome")
##
##
##class strongnum():
##    def __init__(self):
##        pass
##    def check(self,num):
##        n1=num
##        sm=0
##        while(num!=0):
##            rem=num%10
##            f=1
##            for i in range(1,rem+1):
##                f=f*i
##            sm=sm+f
##            num=num//10
##
##        if (n1==sm):
##            return True
##        else:
##            return False
##
##stg = strongnum()
##num = 145
##
##if(stg.check(num)):
##    print("strong num")
##else:
##    print("not strong num")



##class Armstrongnum():
##    def __init__(self):
##        pass
##
##    def check (self,num):
##        n1=num
##        n2=num
##        sm=0
##        c=0
##
##        while (num!=0):
##            num=num//10
##            c=c+1
##        while (n1!=0):
##            rem=n1%10
##            sm=sm+rem**c
##            n1=n1//10
##
##        if(n2==sm):
##            return True
##        else:
##            return False
##
##am = Armstrongnum()
##
##num= int(input("Enter a number : "))
##
##if (am.check(num)):
##    print("armstrong")
##else:
##    print("not armstrong")



class neon():
    def __init__(self):
        pass
    def check(self,num):
        sq=num*num
        sm=0
        while(sq!=0):
            rem=sq%10
            sm=sm+rem
            sq=sq//10

        if(num==sm):
            return True
        else:
            return False

ne=neon()

num=int(input("Enter a numer : "))

if(ne.check(num)):
    print ("this number is neon")
else:
    print ("this number is not neon")
            







































            
