#WAP to find Maximum number, Minimum number, second highest and second lowest
##value from the list without using function and slicing or sorting.

x=[11,1,2,15,17,19,22,7,9,8]

##I. Maximum Number
##def maximum(x):
##    lg=x[0]
##    for i in x:
##        if(lg<i):
##            lg=i
##    return lg

##II.Second highest number

##def secondlg(x):
##    lg=x[0]
##    slg=x[1]
##    for i in x:
##        if(i>lg):
##            slg=lg
##            lg=i
##        elif(i!=lg) and (i>slg):
##            slg=i
##    return slg

##III. Minimum Number

##def smallestnum(x):
##    sm=x[0]
##    for i in x:
##        if(sm>i):
##            sm=i
##    return sm


##IV. second lowest number

def secondsm(x):
    sm=x[0]
    ssm=x[1]
    for i in x:
        if(i<sm):
            ssm=sm
            sm=i
        elif(i!=sm) and (i<ssm):
            ssm=i
    return ssm
