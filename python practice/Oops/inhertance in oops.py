##class employee():
##    def __init__(self,name,age,post,salary): #__init__ function
##        self.name = name
##        self.age = age
##        self.post = post
##        self.salary = salary
##
##    def __str__(self): #__str__ function use to store 
##        return(f" Name : {self.name}\nAge : {self.age}\nPost : {self.post}\nSalary : {self.salary}")
##emp1 = employee("nitin",52,"deo",1000)

#==============================================================================================================

##class university():
##    def __init__(self,name,domain,funds):
##        self.name = name
##        self.domain = domain
##        self.funds = funds
##
##    def __str__(self):
##        return f"{self.name}|{self.domain}|{self.funds}"
##
##class college(university):
##    def __init__(self,name,domain,funds):
##        super().__init__(name,domain,funds)
##
##    def __str__(self):
##        return super().__str__()

#================================================================================

class gf():
    eyes = "blue"
    nose = "parrot"
    voice = "soft"

    def intro(self):
        print("i am gf class")

class f(gf):
    nose = "pig"
    hair = "brown"
    color = "dark"

    def intro(self):
        print("i am f class")
class s(f):
    pass

    def intro(self):
        print("i am s class")
c1=s()


    
