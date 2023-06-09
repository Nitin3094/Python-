import pymysql as p

def getconnect():
    return p.connect(host="localhost", user="root", password="",database="flaskapp")

def insertdata(t):
    db=getconnect()
    cr=db.cursor()
    sql= "insert into users values(%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()
    print("data inserted successfully...!")

def getdata():
    db = getconnect()
    cr = db.cursor()
    sql = "select uname,upin from users"
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
