import tweepy, json

# pip install tweepy

# GET API key from twitter_keys.json
with open("./Part2/TwitterAPI/keys/twitter_keys.json") as json_file:
    json_data = json.load(json_file)

# Store OAuth authentication credentials in relevant variables
access_token = json_data['access_token']
access_token_secret = json_data['access_token_secret']
consumer_key = json_data['consumer_key']
consumer_secret = json_data['consumer_secret']


# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

