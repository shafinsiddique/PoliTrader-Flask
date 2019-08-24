from flask import Flask
from flask import render_template
from pymongo import MongoClient
from DBHelper import ScoresCollectionHelper
from MainController import MainController
app = Flask(__name__)

client = MongoClient("mongodb+srv://shafinsiddique:password@politradercluster-zpqob.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("sentiments")
collectionHelper = ScoresCollectionHelper(db.politicians)

mainController = MainController(ScoresCollectionHelper)

@app.route("/")
def homePage():
    return render_template("home.html", stocks=MainController.getAllStocks)




