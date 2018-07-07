import tweepy
from textblob import TextBlob

Consumer_Key ='_____'
Consumer_Secret = '_____'
Access_Token = '_____'
Access_Token_Secret = '_____'

auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)

api=tweepy.API(auth)
tweets=str(input("Enter any tweet "+"\n"))
print("You Entered String is :"+ tweets+"\n")
public_tweets=api.search(tweets)

for tweets in public_tweets:
	print(tweets.text)
	analysis=TextBlob(tweets.text)
	print(analysis.sentiment)
