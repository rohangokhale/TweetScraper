import tweepy
import settings

CONSUMER_KEY = 'iFtEL4v7OPKQOYFdtKk4FYR5Q'
CONSUMER_SECRET = 'ec3rJwGb8yrUe76f5evnYf9c3hohecLARHWgTVuJWl4N7QCyJS'
ACCESS_TOKEN = '826083922685657089-jkLYZ5lUMcNqnDBWRdRNyUSm0uCisaI'
ACCESS_TOKEN_SECRET = 'QXp9RorcwvDwzOiyxqQmB5RTsM1yClHHgaGFbZVECaUco'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

statusupdate = "Testing!2"
api.update_status(status=statusupdate)
