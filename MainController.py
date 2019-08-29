from User import User
class MainController:
    def __init__(self, priceCollectionHelper, userCollectionHelper):
        self.pricecollectionhelper = priceCollectionHelper
        self.stocks = self.pricecollectionhelper.getAllStocks()
        self.usercollectionhelper = userCollectionHelper

    def getStocksJson(self):
        return [stocks.toJson() for stocks in self.stocks]

    def getAllStocks(self):
        return self.stocks

    def findStock(self, name):
        for stocks in self.stocks:
            if (stocks.name == name):
                return stocks

    def registerUser(self, username, email, password):
        self.usercollectionhelper.addUser(username, email, password)

    def createUser(self, userDict):
        user = User(userDict['username'], userDict['email'],
                    userDict['stocks'], userDict['invested'],
                    userDict['balance'])

        return user







