#WAP to check whether the given number is strong or not
n=int(input("Enter your number : "))
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
    print("This number is strong")
else:
    print("This number is not strong")
