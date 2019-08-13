from User import User
class Portal:
    def __init__(self):
        self.stocks = []
        self.user = User()


    def run(self):
        self.showHomePage()

    def displayStocks(self):
        for stocks in self.stocks:
            print(stocks)
    def showHomePage(self):
        activity = input("What would you like to do?\n"
                         "1.View stocks and buy them."
                         "2.View dashboard\n"
                         "2.View your transaction history\n")

        if (activity == 1):
            self.displayStocks()
