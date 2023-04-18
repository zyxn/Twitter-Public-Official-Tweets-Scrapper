import snscrape.modules.twitter as sntwitter
import pandas as pd

# Set search parameters
candidates = ['prabowo', 'ganjarpranowo', 'aniesbaswedan','puanmaharani_ri','AgusYudhoyono']


# Scrape tweets
tweets = []
for x in range(len(candidates)):
    query = f"(to:{candidates[x]}) until:2023-04-18 since:2022-01-01 "
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        date = tweet.date.strftime('%Y-%m-%d %H:%M:%S')
        username = tweet.username
        text = tweet.content
        location = tweet.user.location if hasattr(tweet.user, 'location') else ''
        tweets.append((date, username, text, location))
        
        # Limit number of tweets to 1000 for demonstration purposes
        
        if i >= 1000:
            break

# Convert to pandas dataframe
df = pd.DataFrame(tweets, columns=['date', 'username', 'text', 'location'])
print(df.head(5))
df.to_csv("hasil.csv", sep=";", encoding="utf-8",quoting=2 ,index=False)