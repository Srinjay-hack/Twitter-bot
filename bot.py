import tweepy
import time




print('this is my twitter bot', flush=True)


CONSUMER_KEY = 'XXXXX'
CONSUMER_SECRET = 'YYYYYYYYY'
ACCESS_KEY = 'ZZZZZZZZ'
ACCESS_SECRET = 'AAAAAAAAAAAA'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


file_name = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply():


    tweets=api.mentions_timeline(retrieve_last_seen_id(file_name),tweet_mode='extended')


    for tweet in  reversed(tweets):

        if "#helloworld" in tweet.full_text.lower():
            print(str(tweet.id)+'-'+tweet.full_text)

            api.update_status('@' + tweet.user.screen_name +'#HelloWorld back to you!', tweet.id)

            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen_id(tweet.id, file_name)





while(True):
    reply()
    time.sleep(15)






