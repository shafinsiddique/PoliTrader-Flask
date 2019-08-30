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

    def purchaseStock(self, user, stockname):
        stock = self.findStock(stockname)
        user.buyStock(stock)
        self.usercollectionhelper.buyStock(user, stock)

    def sellStock(self, user, stockname, purchasedPrice):
        user.sellStock(stockname, purchasedPrice)
        user.addToBalance(self.getPriceDictionary()[stockname])
        self.usercollectionhelper.sellStock(user, stockname,
                                            purchasedPrice)

    def getPriceDictionary(self):
        stocksPrices = {}
        for stocks in self.stocks:
            stocksPrices[stocks.name] = stocks.getCurrentPrice()

        return stocksPrices

    def getChanges(self, userStocks):
        changesDict = {}
        priceDict = self.getPriceDictionary()
        for stocks in userStocks:
            changesDict[stocks['name']] = round(((priceDict[stocks['name']]-\
                                          stocks['currentPrice'])/stocks['currentPrice'])*100,2)

        return changesDict

    def getPV(self, user):
        currentPriceDict = self.getPriceDictionary()
        portfolioValue = 0
        for stocks in user.stocks:
            portfolioValue += currentPriceDict[stocks['name']]

        return portfolioValue

    def getProfit(self, user):
        return self.getPV(user) - user.invested

    def getProfitPercent(self, user):
        return round(((self.getPV(user) - user.invested)/user.invested)*100,2)
    def getUserDict(self, user):
        userDict = user.toJson()
        userDict['portfolioValue'] = self.getPV(user)
        userDict['profit'] = self.getProfit(user)
        userDict['profitPercent'] = self.getProfitPercent(user)

        return userDict

    def getRankings(self):
        rankingsDict = {}
        allUsers = self.usercollectionhelper.getAllUsers()

        for users in allUsers:
            rankingsDict[users.username] = self.getProfit(users)

        return sorted(rankingsDict.items(), key=lambda x: x[1], reverse=True)

