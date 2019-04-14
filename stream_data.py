import os
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from info import data

CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


class listener(StreamListener):
    def on_connect(self):
        print('Stream starting...')

    def on_status(self, status):
        if status.geo is not None:
            t = dict()
            t['text'] = status.text
            t['coordinates'] = status.coordinates
            print(t['text'])
            data.append(t)

    def on_error(self, status):
        print(status)


def main():
    twitterStream = Stream(auth, listener())
    twitterStream.filter(
        locations=[
            -73.3049515449, 0.724452215982, -59.7582848782, 12.1623070337
        ],
        track=['sinluz', 'venezuela', 'maldito maduro',
               'maracay', 'caracas', 'sininternet', 'sinnada']
    )
