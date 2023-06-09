#WAP to calculate sum of digits input -7546 output=22
n=int(input("Enter your number : "))
sm=0
while(n!=0):
    rem=n%10
    sm=sm+rem
    n=n//10
    print("Sum = ",sm)
