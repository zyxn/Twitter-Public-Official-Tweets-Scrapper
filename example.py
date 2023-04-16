import snscrape.modules.twitter as sntwitter
import numpy as np
import pandas as pd

query = "(to:puanmaharani_ri) until:2023-04-16 since:2022-04-16 filter:replies"
limit = 200

tweets = np.empty((limit, 3), dtype=object)
index = 0

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if index == limit:
        break
    else:
        tweets[index, 0] = tweet.date
        tweets[index, 1] = tweet.username
        tweets[index, 2] = tweet.content
        index += 1

tweets = tweets[:index, :]  # menghapus baris yang tidak terisi pada array

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
df['Tweet'] = df['Tweet'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii'))
df.to_csv("hasil.csv", sep=";", encoding="utf-8", index=False)