from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from pymongo import MongoClient
from flask import url_for
from DBHelper import ScoresCollectionHelper, UserCollectionHelper
from MainController import MainController
from forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from flask import flash
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
client = MongoClient("mongodb+srv://shafinsiddique:@politradercluster-zpqob.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("sentiments")
scorecollectionHelper = ScoresCollectionHelper(db.politicians)
userCollectionHelper = UserCollectionHelper(db.users)
mainController = MainController(scorecollectionHelper, userCollectionHelper)
bcrypt = Bcrypt(app)
user = None

@app.route("/")
def homePage():
    return render_template("home.html", stocks=mainController.getStocksJson())

@app.route("/stock/<name>")
def stockPage(name):
    s = mainController.findStock(name)
    return render_template("stocksPage.html", labels=s.dates,
                           prices = s.pricesWD, name=s.name)
@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        mainController.registerUser(form.username.data, form.email.data,
                                    bcrypt.generate_password_hash(form.password.data).
                                    decode('utf-8'))
        flash(f'Account created for {form.username.data}', 'success')

        return redirect(url_for("login"))

    return render_template("registration.html", form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        queryUser = userCollectionHelper.findUser(form.username.data)
        if queryUser and bcrypt.check_password_hash(queryUser['password'],

                                              form.password.data):
            global user
            user = mainController.createUser(queryUser)
            return redirect(url_for('userHome'))
        else:
            flash(f"invalid credentials.","success")


    return render_template("login.html", form=form)

@app.route("/home", methods=['GET','POST'])
def userHome():
    if user:
        return render_template("userHome.html", user=user.toJson())

    else:
        return homePage()


@app.route("/market", methods=['GET','POST'])
def market():
    if user:

        if request.method == "POST":
            stockname = request.form['buy']
            mainController.purchaseStock(user, stockname)

            flash(f"You have successfully purchased a share of {stockname}",
                  'success')

        return render_template("market.html",
                               stocks=mainController.getStocksJson())
    else:
        return homePage()









