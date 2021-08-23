import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("machine learning")
tweet = public_tweets[0]
for tweet in public_tweets:
    status = api.get_status(tweet.id, tweet_mode="extended")
    try:
        api.create_friendship(tweet.user.id)
        api.retweet(tweet.id)
        # print(status.retweeted_status.full_text)
    except AttributeError:  # Not a Retweet
        print(status.full_text)
