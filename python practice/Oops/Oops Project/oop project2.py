class user():
    def __init__(self,name,gender,salary):
        self.name = name
        self.gender = gender
        self.salary = salary
    
    def showdetails(self):
        return(f"Name : {self.name}\nGender : {self.gender}\nSalary : {self.salary}")

class bank():
    def __init__(self,name,gender,salary):
        self.name =name
        self.gender = gender
        self.salary = salary
        self.__balance = 0
        
    def deposite(self,amount):
        self.amount = amount
        self.__balance=self.__balance+self.amount
        
    def withdraw(self,amount):
        self.amount = amount
        if(self.amount>self.__balance):
            return ("insuffient balance","Current Balance : ",self.__balance)
        elif(self.amount>=100 and self.amount<=self.__balance):
            self.__balance = self.__balance - self.amount
            return ("Thank you for visiting","Current Balance: ",self.__balance)
        elif(self.amount<100):
            return ("you cannot withdraw less then 100","Current Balance : ",self.__balance)
    def viewbalance(self):
         return (f"Name : {self.name}\nGender : {self.gender}\nSalary: {self.salary}\nBalance: {self.__balance}")
    def transfer(self,amount,user):
        self.amount = amount
        self.user = 0
        if (self.amount>self.__balance):
            return("insufficient balance","Current Balance",self.__balance,"user : ",self.user)
        elif (self.amount>=1 and self.amount<=self.__balance):
            self.__balance = self.__balance - self.amount
            self.user = self.user + self.amount
            return ("Amount transferred successfully","Current Balance : ",self.__balance,"User : ",self.user)
        elif(self.amount<1):
            return ("you cannot transfer less than 1","Current Balance",self.__balance,"user : ",self.user)

obj=user("nitin","male",14000)
obj1=bank("nitin","male",15000)








        

