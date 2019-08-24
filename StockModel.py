from mongoengine import Document
from mongoengine import connect
import mongoengine
a = connect(host='mongodb+srv://shafinsiddique:password@politradercluster-zpqob.mongodb.net/test?retryWrites=true&w=majority')
class Stock(Document):
    name = mongoengine.StringField()
    prices = mongoengine.ListField(mongoengine.ListField())
    meta = {'collection': 'politicians'}





stocks = Stock()
stocks.name = "oweif"
stocks.prices = []
stocks.save()




