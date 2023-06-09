#WAP which takes an rithmetic operators & 2 numbers, as an an do the calculation based on the input operators

x=int(input("Enter your Number : "))
y=int(input("Enter your Number : "))
z=input("Enter your Operator : ")

if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
elif z=="/":
    print(x/y)
else :
    print("invalid operator")
    
