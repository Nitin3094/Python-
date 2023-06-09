#WAP to check whether the given number is palindrome or not
n=int(input("Enter a number : "))
rev=0
n1=n
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10

if(n1==rev):
    print("Palindrome number")
else:
    print("Not palindrome number")
    
