import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score

np.random.seed(500)

def preprocess_text(dataset):
    # Step - a : Remove blank rows if any.
    dataset['text'].dropna(inplace=True)
    # Step - b : Change all the text to lower case. This is required as python interprets 'dog' and 'DOG' differently
    dataset['text'] = [entry.lower() for entry in dataset['text']]
    # Step - c : Tokenization : In this each entry in the corpus will be broken into set of words
    dataset['text'] = [word_tokenize(entry) for entry in dataset['text']]
    tag_map = defaultdict(lambda: wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV
    for index, entry in enumerate(dataset['text']):
        # Declaring Empty List to store the words that follow the rules for this step
        Final_words = []
        # Initializing WordNetLemmatizer()
        word_Lemmatized = WordNetLemmatizer()
        for word, tag in pos_tag(entry):
            if word not in stopwords.words('english') and word.isalpha():
                word_Final = word_Lemmatized.lemmatize(word, tag_map[tag[0]])
                Final_words.append(word_Final)
        dataset.loc[index, 'text_final'] = str(Final_words)

dataset = pd.read_csv("dataset.csv",encoding='latin-1')
preprocess_text(dataset)

Train_X, Test_X, Train_Y, Test_Y = \
    model_selection.train_test_split(dataset['text_final'],dataset['label'],test_size=0.3)

Encoder = LabelEncoder()
Train_Y = Encoder.fit_transform(Train_Y)
Test_Y = Encoder.fit_transform(Test_Y)

Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(dataset['text_final'])
Train_X_Tfidf = Tfidf_vect.transform(Train_X)
Test_X_Tfidf = Tfidf_vect.transform(Test_X)

Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Tfidf,Train_Y)
# predict the labels on validation dataset
predictions_NB = Naive.predict(Test_X_Tfidf)
# Use accuracy_score function to get the accuracy
print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, Test_Y)*100)