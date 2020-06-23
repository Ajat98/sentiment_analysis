from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Consumer key, consumer secret, access token, access secret
#From aps.twitter.com
ckey = 'ckey here'
csecret = 'ssecret here'
atoken = 'atoken here'
asecret = 'asecret here'

class listener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)