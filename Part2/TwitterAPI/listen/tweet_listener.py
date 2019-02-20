import tweepy, json

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("./Part2/TwitterAPI/tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    # def on_data(self, data):
    #     print(data)
        # with open("Output.txt", "w") as text_file:
        #     print(data, file=text_file)
        # return True

    def on_error(self, status):
        print(status)