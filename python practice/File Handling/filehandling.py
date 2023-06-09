def read():
    with open("story.txt","r") as file:
        file = file.readlines()
        return file


def count():
    count = 0
    with open("story.txt","r") as file:
            for line in file:
                if(not line.startswith("T")):
                    count=count+1
            return count
        
def displaywords(): 
    with open("story.txt","r") as file:
        file = file.readlines()
        for line in file:
            for words in line.split():
                if (len(words)<4):
                    print words
            
def copy():
    with open("story.txt","r") as f1:
        with open("story2.txt","w") as f2:
            for data in f1:
                f2.write(data)
        
