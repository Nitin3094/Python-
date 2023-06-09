#1.using list comprehension store all the even numbers from 1 to 100 in a list

##even=[]
##for i in range(1,101):
##    if(i%2==0):
##        even.append(i)

#LC => even=[i for i in range(1,101) if(i%2==0)]

#2.using list comprehension store all leap year from 1900 to 2030 in a list

##year=[]
##for i in range(1900,2030):
##    if(i%400==0) or (i%4==0 and i%100!=0):
##        year.append(i)

##LC => year=[i for i in range(1900,2030) if(i%400==0) or (i%4==0 and i%100!=0)]

#3.using list comprehension store cubes of natural number from 1-20 in a list

##cube=[]
##for i in range(1,20):
##    cube.append(i**3)

# LC => cube=[i**3 for i in range(1,20)]

#4.library=[("book1",2002),("book2",2012),("book3",2007),("book4",2015),("book5",2005),("book6",2018)]
#given a list lib,using list comprehension store all the books that was published after 2010.

##Data=[]
##for book,year in library:
##    if(year>2010):
##        Data.append((book,year))

#LC => Data=[((book,year)) for book,year in library if(year>2010)]

#5. Grammer=["is","not","am","are","do","did","no","will","never","shall","none","was","nor"]

##nv=[]
##for words in Grammer:
##    if(words.startswith("n")):
##        nv.append(words)

#LC => nv=[words for words in Grammer if(words.startswith("n"))]
