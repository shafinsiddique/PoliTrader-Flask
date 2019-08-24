from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/")
def homePage():
    d = {"name": "shafin"}
    return render_template("home.html",d)




