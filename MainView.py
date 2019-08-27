from flask import Flask
from flask import render_template
from pymongo import MongoClient
from DBHelper import ScoresCollectionHelper
from MainController import MainController
app = Flask(__name__)

client = MongoClient("mongodb+srv://shafinsiddique:@politradercluster-zpqob.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("sentiments")
collectionHelper = ScoresCollectionHelper(db.politicians)

mainController = MainController(collectionHelper)
@app.route("/")
def homePage():
    return render_template("home.html", stocks=mainController.getStocksJson())

@app.route("/stock/<name>")
def stockPage(name):
    return name










