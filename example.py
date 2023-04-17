import snscrape.modules.twitter as sntwitter
import pandas as pd

# Set search parameters
candidates = ['Prabowo Subianto', 'Agus Harimurti Yudhoyono', 'Anies Baswedan','Puan Maharani']
query = f"{' OR '.join(candidates)} since:2022-01-01 until:2023-04-17"

# Scrape tweets
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    date = tweet.date.strftime('%Y-%m-%d %H:%M:%S')
    username = tweet.username
    text = tweet.content
    #mastah ami
    # print(tweet.user.descriptionLinks)
    birthday = tweet.user.birthdate if hasattr(tweet.user, 'birthdate') else ''
    location = tweet.user.location if hasattr(tweet.user, 'location') else ''
    tweets.append((date, username, text, birthday, location))
    
    # Limit number of tweets to 1000 for demonstration purposes
    if i >= 1000:
        break

# Convert to pandas dataframe
df = pd.DataFrame(tweets, columns=['date', 'username', 'text', 'birthday', 'location'])
print(df.head(5))
df.to_csv("hasil.csv", sep=";", encoding="utf-8", index=False)