from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from unidecode import unidecode


conn = sqlite3.connect('twitter.db')
c = conn.cursor()
def create_table():
    #need to convert unix time (ms) into date or regular time
    c.execute('CREATE TABLE IF NOT EXISTS sentiment (unix REAL, tweet TEXT, sentiment REAL)')
    conn.commit()

create_table()

#Consumer key, consumer secret, access token, access secret
#From aps.twitter.com
ckey = 'ckey here'
csecret = 'ssecret here'
atoken = 'atoken here'
asecret = 'asecret here'

class listener(StreamListener):
    
    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            analysis = TextBlob(line)
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(time_ms, tweet, sentiment)
            c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)", (time_ms, tweet, sentiment))
            conn.commit()
        except KeyError as e:
            print(str(e))
        return (True)

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
#Streams things for the term 'car' can be changes
twitterStream.filter(track=['car'])
