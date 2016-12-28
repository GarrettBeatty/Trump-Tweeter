import twitter
from keys import cons_key, cons_secret, access_sec, access_tok
import markovify
import nltk
import re

api = twitter.Api(consumer_key=cons_key,
	consumer_secret=cons_secret,
	access_token_key=access_tok,
	access_token_secret=access_sec)

corpus = open("tweets.txt").read()
text_model = markovify.Text(corpus, state_size=2)

status = text_model.make_short_sentence(140)

api.PostUpdate(status)