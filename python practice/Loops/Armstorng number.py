#WAP to check whether the given number is armstrong or not
n=int(input("Enter your number : "))
sm=0
n1=n
n2=n
c=0
while(n!=0):
    n=n//10
    c=c+1

while(n1!=0):
    rem=n1%10
    sm=sm+rem**c
    n1=n1//10

if(n2==sm):
    print("Armstrong number")
else:
    print("Not armstrong number")
