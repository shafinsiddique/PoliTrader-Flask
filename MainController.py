class MainController:
    def __init__(self, priceCollectionHelper):
        self.pricecollectionhelper = priceCollectionHelper


    def getAllStocks(self):
        self.pricecollectionhelper.getAllStocks()


