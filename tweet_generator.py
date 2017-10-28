#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
import unicodedata
import re
import os.path
import markovify

# Twitter API credentials
consumer_key = 'TelkaEC2GUWR0IJogWxkrpZKy'
consumer_secret = 'ENYYJseZJ1IY0wqXUSnEj0i2L0Xz3v2c6MRvPEzY6hnrt3ZEEj'
access_token = '1620837440-0p8voswXhMYGO8upThRqeGwzUuh3TI9sPnQkZim'
access_secret = 'obvlWiW1Tvkdl1JYyA6hbIrJ96yvq1OS2hILRHs3R0HHy'


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    #new_tweets = api.user_timeline(screen_name=screen_name, count=200, q='-filter:links')
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print
        "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print
        "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv
    pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    outtweets = []
    for tweet in alltweets:
        if "RT" not in tweet.text:
            t = unicodedata.normalize('NFKD', tweet.text).encode('ascii', 'ignore')
            t = t.decode('utf-8')
            t = t.replace("\n"," ")
            pattern.sub('',t)
            outtweets.append([t])

    # write the csv
    with open("%s_tweets.csv" % screen_name, "wt") as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)
    pass

if __name__ == '__main__':
    # pass in the username of the account you want to download
    user = "realDonaldTrump"

    if not os.path.isfile("%s_tweets.csv" % user):
        get_all_tweets(user)

    # Get raw text as string.
    with open("%s_tweets.csv" % user) as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(20):
        print(text_model.make_short_sentence(140))