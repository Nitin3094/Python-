import pymysql as p
def getconnect():
    return p.connect(host="localhost",user="root", password="",database="thisdb")
def insertdata(t):
    db = getconnect()
    cr = db.cursor()
    sql = "insert into mytable values(%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()
    print("data inserted successfully......!")

def updatedata(t):
    db = getconnect()
    cr = db.cursor()
    sql = "update mytable set name=%s,position=%s,rating=%s,salary=%s,age=%s,city=%s where id=%s"
    cr.execute(sql,t)
    db.commit()
    db.close()
    print("data updated successfully...!")

t =("nitin","IT",8.8,1000,28,"mumbai",2)
updatedata(t)

    
