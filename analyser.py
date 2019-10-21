import tweepy
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

#your keys
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Search parameter
api = tweepy.API(auth)
train = [('This sandwich is from heaven', 'pos'), ('this is an amazing place!', 'pos'), ('Great night out', 'pos'), ('this is the best day ever!', 'pos'), ("what an awesome view", 'pos'), ('I am not a fan', 'neg'), ('I am tired of this stuff.', 'neg'), ("can't deal with this", 'neg'), ('i hate that!', 'neg'),    ('ugh this is horrible.', 'neg') ]
cl = NaiveBayesClassifier(train)

#Search for tweets about anything
public_tweets = api.search('New York')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text,classifier=cl)
    print(analysis.classify())

