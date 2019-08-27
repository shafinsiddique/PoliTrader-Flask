class Stock:
    def __init__(self, name, ticker, prices):
        self.name = name
        self.ticker = ticker
        self.prices = prices
        self.pricesWD = [price[1] for price in self.prices]
        self.dates = [price[0] for price in self.prices]


    def toJson(self):
        return {"name":self.name, "ticker":self.ticker, "prices": self.pricesWD,
                "currentPrice": self.getCurrentPrice(),"change": self.getChange()}

    def getCurrentPrice(self):
        if len(self.pricesWD) > 0:
            return self.pricesWD[-1]

        else:
            return 0
    def getChange(self):
        if len(self.pricesWD) > 1:
            return round(((self.pricesWD[-1] - self.pricesWD[-2])/self.pricesWD[-2])*100, 2)

        else:
            return 0




