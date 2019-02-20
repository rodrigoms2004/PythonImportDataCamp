import tweepy

from listen.tweet_listener import MyStreamListener
from tw_auth import auth

# Create Streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth, l)

# this line filters Twitter Streams to capture data by keywords:
stream.filter(track=['apples', 'oranges'])
