# Star print using nested loop

row=4

##for i in range(1,5):
##    for j in range(1,i+1):
##        print("*", end=" ")
##    print()

##for i in range(1,row+1):
##    for j in range(row,i-1,-1):
##        print("*", end=" ")
##    print()

for i in range(1,row+1):
    for j in range(row-1,i-1,-1):
        print(" ", end=" ")
    for k in range(1,i+1):
        print("*", end=" ")
    print()

    
