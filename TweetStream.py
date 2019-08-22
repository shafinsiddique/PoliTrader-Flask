from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import preprocessor as p
import re
from pymongo import MongoClient
from sentiments import get_sentiments
from DBHelper import ScoresCollectionHelper
from datetime import datetime

ACCESS_TOKEN ="ENTERKEY"
ACCESS_TOKEN_SECRET ="ENTERKEY"
CONSUMER_KEY = "ENTERKEY"
CONSUMER_SECRET = "ENTERKEY"

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True,
          wait_on_rate_limit_notify=True)


def clean_tweet(tweet: str):
    preprocess = p.clean(tweet)
    preprocess = re.sub(r'[^\w\s]','',preprocess)

    return preprocess


class Listener(StreamListener):

    def __init__(self, CollectionHelper):
        StreamListener.__init__(self)
        self.count = 0
        self.sentimentscore = 0
        self.collectionHelper = CollectionHelper
        self.currentSubject = None

    def on_data(self, data):
        all_data = json.loads(data)
        tweet  = clean_tweet(all_data['text'])
        print(str(self.count) + ". " + tweet)
        self.sentimentscore += get_sentiments([tweet])[0]
        self.count += 1

        if (self.count > 20):
            print("Score: " + str(self.sentimentscore))
            collectionHelper.appendScore(self.currentSubject, datetime.now(),
                                         int(self.sentimentscore))
            print(self.currentSubject + " score has been calculated and added to database.")
            self.count = 0
            self.sentimentscore = 0
            return False
        else:
            return(True)

    def on_error(self, status):
        print(status)

    def setSubject(self, subjectName):
        self.currentSubject = subjectName


def calculateScoreForSubjectsandUpdateDatabase(listener: Listener,
                                               stream: Stream, subjects: list):
    for subject in subjects:
        listener.setSubject(subject)
        stream.filter(track=[subject], languages=['en'])

if __name__ == "__main__":

    client = MongoClient("ENTERCREDENTIALS")
    db = client.get_database("sentiments")

    collectionHelper = ScoresCollectionHelper(db.politicians)

    Listener = Listener(ScoresCollectionHelper)

    twitterStream = Stream(auth, Listener)

    subjects = collectionHelper.getAllSubjects()

    calculateScoreForSubjectsandUpdateDatabase(Listener, twitterStream, subjects)


