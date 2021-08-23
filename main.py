import tweepy
from identity import Identity

identity = Identity()

auth = tweepy.OAuthHandler(identity.consumer_key, identity.consumer_secret)
auth.set_access_token(identity.access_token, identity.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("machine learning")
for tweet in public_tweets:
    status = api.get_status(tweet.id, tweet_mode="extended")
    try:
        api.create_friendship(tweet.user.id)
        api.retweet(tweet.id)
        # print(status.retweeted_status.full_text)
    except AttributeError:  # Not a Retweet
        print(status.full_text)
