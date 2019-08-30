class User:
    def __init__(self, username, email, stocks, invested, balance):
        self.username = username
        self.email = email
        self.stocks = stocks
        self.invested = invested
        self.balance = balance

    def toJson(self):
        return {"username":self.username,
                "email": self.email,
                "stocks":self.stocks,
                "invested":self.invested,
                "balance":self.balance,
                "profit":0}

    def buyStock(self, stock):
        self.stocks.append(stock.toJson())
        self.invested += stock.getCurrentPrice()
        self.balance -= stock.getCurrentPrice()
    def getPurchasedStocks(self):
        names  = []
        for stocks in self.stocks:
            names.append(stocks['name'])

        return names

    def sellStock(self, stockname,  purchasedPrice, currentPrice):
        for x in range(len(self.stocks)):
            if (self.stocks[x]['name'] == stockname):
                if (self.stocks[x]['currentPrice'] == int(purchasedPrice)):
                    self.stocks.pop(x)
                    break
        self.invested -= purchasedPrice
        self.balance += currentPrice







