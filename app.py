from flask import Flask,request,jsonify
import smtplib
import os
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['POST'])
@cross_origin(headers=['Content-Type'])
def index():
    if request.method=="POST":
        try:
            msg=f"Subject:{request.form.get('category')}"+"\n\nFrom: "+request.form.get("name")+"\nemail: "+request.form.get("email")+"\n\nmessage: "+request.form.get("message")
            fromaddr="updates.teamfateh@gmail.com"
            password=os.getenv(password)
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(fromaddr, password)
            server.sendmail(fromaddr, ["team.fateh@thapar.edu","aryankhera11@gmail.com"], msg)
            server.quit()
            return(jsonify(sent="success"),200)
        except:
            return(jsonify(sent="failed"),200)
    else:
        return("Method not allowed",405)
