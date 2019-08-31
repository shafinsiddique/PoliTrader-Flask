# PoliTrader

PoliTrader is an online trading simulator in which instead of trading shares in companies, users can trade shares in 
POLITICIANS. The 'market price' of the politician is based on their sentiment on twitter. If the public is tweeting positively
about them, their market price goes up and if the public tweets negatively about them, their market price goes down.

The main purpose of this application is to provide young adults with an innovative and fun way of keeping up with current events.

PoliTrader is built using Python's Flask Framework. The sentiment analysis of tweets is done using a text classification model. The model was trained using Sci-Kit Learn and NLTK, Python's natural language processing library.

![Tickers Page](https://user-images.githubusercontent.com/41314351/64060302-aaa63e80-cb98-11e9-9a19-2cff4725898d.png)
![Stock Chart](https://user-images.githubusercontent.com/41314351/64060303-b72a9700-cb98-11e9-8d51-080517cf4163.png)
![Dashboard](https://user-images.githubusercontent.com/41314351/64060513-b6473480-cb9b-11e9-841c-986a626e5627.png)
![Investments](https://user-images.githubusercontent.com/41314351/64060312-d3c6cf00-cb98-11e9-9e69-070cc629351f.png)
![MarketPlace](https://user-images.githubusercontent.com/41314351/64060314-d75a5600-cb98-11e9-957f-4f6bb31ade38.png)
![Rankings](https://user-images.githubusercontent.com/41314351/64060319-dfb29100-cb98-11e9-8c73-6ef37be37ab0.png)


## Features

- Get a quantitative value representing the public's sentiment about a politician.
- View the politicians sentiment graph.
- Create an account to invest in politicians. Users can buy shares in politicians that they believe will perform well and later on sell those shares.
- Users can also compete with other users and view their world ranking. Rankings are based on the amount of net profit.

## Requirements

- Flask, Flask-Bcrypt, PyMongo Libraries.
- MongoDB
- Twitter API Key.






