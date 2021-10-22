import datetime
import time

import tweepy as twitter

import keys
import random

auth = twitter.OAuthHandler(keys.api_key, keys.api_secret)
auth.set_access_token(keys.access_key, keys.access_secret)
api = twitter.API(auth)


def twitter_bot_retweet(hashtag, delay):
    while True:
        print(f'\n{datetime.datetime.now}/n')

        for tweet in twitter.Cursor(api.search_tweets, q=hashtag, count=500).items(25):
            try:
                tweet_id = dict(tweet._json)['id']
                tweet_text = dict(tweet._json)['text']

                print('id: ' + str(tweet_id))
                print('text: ' + str(tweet_text))

                api.retweet(tweet_id)

            except twitter.TweepyException as error:
                print(error)

        time.sleep(delay)


def twitter_bot_like(hashtag, delay):
    while True:
        print(f'\n{datetime.datetime.now}/n')

        for tweet in twitter.Cursor(api.search_tweets, q=hashtag, count=1000).items(100):
            try:
                tweet_id = dict(tweet._json)['id']
                tweet_text = dict(tweet._json)['text']

                print('id: ' + str(tweet_id))
                print('text: ' + str(tweet_text))

                api.create_favorite(tweet_id)

            except twitter.TweepyException as error:
                print(error)

        time.sleep(delay)


hashtags = ['#etherium', '#solana', '#bitcoin', '#airdrop']

twitter_bot_retweet(random.choice(hashtags), 60)
twitter_bot_like(random.choice(hashtags), 45)
