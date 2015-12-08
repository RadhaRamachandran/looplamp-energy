import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


# Authentication
# from BrannonDorsey LoopLamp Project
consumer_key = "TroyIuC1l3i3laNlwl5mg"
consumer_secret = "qYRSTEHzHhTsL0CBcMnXxjqeY5UQ6U4C0kNvmPSG4K4"
access_token = "1230084602-UtUB4QdlhNkv1aLqrjS3eYoZ96APon5IhjOqBFt"
access_secret = "wscl1nV8gFO4kMhtJy7DjhQKkpJHB1fW5Jzb4RXZq8"
   
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#Streaming API Listner
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('twitter_out.json', 'a') as f:  #set output filename here
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
        
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#energy']) #set hashtag here