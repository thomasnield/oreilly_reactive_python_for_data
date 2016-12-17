from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from rx import Observable

# Variables that contains the user credentials to access Twitter API
access_token = "CONFIDENTIAL"
access_token_secret = "CONFIDENTIAL"
consumer_key = "CONFIDENTIAL"
consumer_secret = "CONFIDENTIAL"


def tweets_for(topics):

    def observe_tweets(observer):
        class TweetListener(StreamListener):
            def on_data(self, data):
                observer.on_next(data)
                return True

            def on_error(self, status):
                observer.on_error(status)

        # This handles Twitter authetification and the connection to Twitter Streaming API
        l = TweetListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=topics)

    return Observable.create(observe_tweets).share()


topics = ['Britain','France']

tweets_for(topics).map(lambda d: json.loads(d)) \
    .filter(lambda map: "text" in map) \
    .map(lambda map: map["text"].strip()) \
    .subscribe(lambda s: print(s))
