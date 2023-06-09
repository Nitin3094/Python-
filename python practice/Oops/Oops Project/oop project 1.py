class Character():
    def __init__(self,name):
        self.name = name
        self.__life = 3
        self.__score = 0

    def kicked(self):
        self.__score = self.__score + 10
    def punched(self):
        self.__score = self.__score + 5
    def stabbed(self):
        self.__life = self.__life -1

    def displaylife(self):
        return self.__life
    def displayscore(self):
        return self.__score
    def __str__(self):
        return (f"Name : {self.name}\nLife : {self.__life}\nScore : {self.__score}")

Mario = Character("Nitin")
Mario = Character("Seema")

Mario.kicked()
Mario.kicked()
Mario.stabbed()
Mario.punched()
Mario.punched()
Mario.stabbed()
Mario.stabbed()
print(Mario)

v=Mario.displaylife()
if(v==0):
    print("Game is Over......!!!")

else:
    print("Welcome to Level 2")
