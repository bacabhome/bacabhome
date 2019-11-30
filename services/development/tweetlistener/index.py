import os, json, time, tempfile, sys, io, urllib, requests, contextlib
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = io.BytesIO()
    yield
    sys.stdout = save_stdout

auth = OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])

class TweetListener(StreamListener):
    def on_data(self, data):
        try:
            tweet = json.loads(data)
            print('Got tweet from %s "%s" (%i followers)' % (tweet['user']['screen_name'], tweet['text'], tweet['user']['followers_count']))
        except Exception as e:
            print("error oops", e)

    def on_error(self, status):
        print('Error from tweet streamer', status)

if __name__ == '__main__':
    print('Setting up')
    l = TweetListener()
    stream = Stream(auth, l)

    print('Listening for tweets')
    stream.filter(track=['@NuupXe'])
