from flask import Flask, render_template, request
from dbm import getdata,insertdata

app = Flask(__name__)

@app.route("/")
def page1():
    return render_template("page1.html")

@app.route("/validuser", methods=["POST"])
def uservalid():
    uname = request.form["uname"]
    pin = request.form["upin"]
    database = getdata()

    if((uname, pin) in database):
        return render_template("page2.html")
    else:
        return render_template("page3.html")

@app.route("/senddata", methods=["POST"])
def send_data():
    uid = request.form["id"]
    uname=request.form["uname"]
    uemail=request.form["uemail"]
    upin=request.form["upin"]

    t= (uid,uname,uemail,upin)
    insertdata(t)

    return render_template("page1.html")

if(__name__=="__main__"):
    app.run(debug=True)
