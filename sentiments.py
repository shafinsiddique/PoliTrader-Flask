import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

dataset = pd.read_csv("dataset.csv")
Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(dataset['text'])
model = pickle.load(open("classifier.sav","rb"))

def get_sentiments(tweets):
    df = pd.DataFrame(tweets, columns=['tweets'], index=None)
    tweetsseries = df['tweets']

    tweets_test = Tfidf_vect.transform(tweetsseries)

    return model.predict(tweets_test)


