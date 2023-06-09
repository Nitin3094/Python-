#WAP to check whether the given number is neon or not
n=int(input("Enter your number : "))
sq=n**2
sm=0

while(sq!=0):
    rem=sq%10
    sm=sm+rem
    sq=sq//10

if(n==sm):
    print("This number is neon")
else:
    print("This number is not neon")
    
