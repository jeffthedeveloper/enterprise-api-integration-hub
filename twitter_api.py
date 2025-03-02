import tweepy

def get_tweets(query):
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.search_tweets(q=query, count=10)
    return [tweet.text for tweet in tweets]

# Exemplo de uso
tweets = get_tweets('Python')
print(tweets)
