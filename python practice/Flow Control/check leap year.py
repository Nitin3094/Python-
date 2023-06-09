#WAP for check a number is leap year or not by using following constraints:-
#1.N div by 400 --> leap year
#2. N div by 4, N not div by 100 --> leap year

N=int(input("Enter Your Number : "))

if(N%400==0):
    print("Leap year")
elif(N%4==0 and N%100!=0):
    print("Leap Year")
else:
    print("not leap year")
