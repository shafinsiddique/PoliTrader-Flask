class MainController:
    def __init__(self, priceCollectionHelper):
        self.pricecollectionhelper = priceCollectionHelper
        self.stocks = self.pricecollectionhelper.getAllStocks()

    def getStocksJson(self):
        return [stocks.toJson() for stocks in self.stocks]

    def getAllStocks(self):
        return self.stocks

    def findStock(self, name):
        for stocks in self.stocks:
            if (stocks.name == name):
                return stocks






