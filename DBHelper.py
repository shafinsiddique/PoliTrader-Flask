from StockModel import Stock


class ScoresCollectionHelper:
    def __init__(self, mongocollection):
        self.mongocollection = mongocollection


    def appendScore(self, subjectname, date, score):
        self.mongocollection.find_one_and_update\
            ({"name": subjectname}, {"$push":{"scores": [date, score]}})

    def getAllSubjects(self):
        cursor = self.mongocollection.find({})
        subjects =[]
        for document in cursor:
            subjects.append(document.get("name"))

        return subjects

    def getAllStocks(self):
        cursor = self.mongocollection.find({})

        stocks = []
        for document in cursor:
            stocks.append(Stock(document.get("name"), document.get("ticker"),
                                document.get("scores")))

        return stocks


class UserCollectionHelper:
    def __init__(self, collection):
        self.mongocollection = collection


    def addUser(self, username, email, password):
        self.mongocollection.insert_one({"username": username,
                                         "email": email,
                                         "password": password,
                                         "stocks":{},
                                         "invested":0,
                                         'balance':100000})

    def findUser(self, username):
        return self.mongocollection.find_one({"username":username})

    def buyStock(self, user, stock):
        query = {"username":user.username}
        self.mongocollection.find_one_and_update(query,
                                                 {"$push":{"stocks":
                                                        stock.toJson()}})

        self.mongocollection.find_one_and_update(query, {"$set":{"invested":
                                                        user.invested}})

    def sellStock(self, user, stockname, purchasedPrice):
        query = {'username': user.username}

        self.mongocollection.find_one_and_update(query,
                                                 {"$pull":{"stocks":
                                            {"name": stockname,

                                            "currentPrice": int(purchasedPrice)}}})

        self.mongocollection.find_one_and_update(query, {"$set":{"balance": user.balance}})

        self.mongocollection.find_one_and_update(query, {"$set":
                                                             {"invested":
                                                                  user.invested}})

