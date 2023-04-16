import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"
tweets = []
limit = 200


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
df.to_csv("hasil.csv",sep=";")