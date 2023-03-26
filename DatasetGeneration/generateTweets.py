import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:ReallySwara) until:2023-03-24 since:2022-10-01"
tweets = []
limit = 2000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)
print(df.head())
