#WAP to reverse a number
#input - 7546
#output - 6457

n=int(input("Enter your number : "))
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    print("Reverse =",rev)
    
