#WAP to display the grade given a mark by using following constraint

marks=float(input("Enter your marks : "))

if(marks>=75):
            print("A grade")
elif(marks>=60 and marks<75):
    print("B grade")
elif(marks>=35 and marks<60):
    print("C grade")
else:
    print("failed")
          
