import tweepy
import random
import lista_respuestas
import os
from keys import consumer_key, consumer_secretkey, acces_secrettoken, access_token

def lambda_handler(event, context):
    consumer_key = os.environ[consumer_key]
    consumer_secretkey = os.environ[consumer_secretkey]
    access_token = os.environ[access_token]
    access_secrettoken = os.environ[access_secrettoken]
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secretkey)
    auth.set_access_token(access_token, access_secrettoken)
    api = tweepy.API(auth)
    
    last_id = 'idultimotwittvisto.txt'
    last_read_id = read_last_tweet(last_id)
    mentions = api.mentions_timeline(since_id = last_read_id, tweet_mode = 'extended')
    
    for mention in reversed(mentions):
        tweet_id = mention.id
        if tweet_id > last_read_id:
            try:
                api.create_favorite(mention.id)
                tweet_text = mention.full_text.lower()
                response = reply_to_tweets(tweet_text)
                api.update_status(status = response, in_reply_to_status_id = tweet_id, auto_populate_reply_metadata = True)
                save_last_tweet(tweet_id, last_id)
            except Exception as e:
                print(e)
                pass

def read_last_tweet(id):
    with open(id, 'r') as f_read:
        last_read = int(f_read.read().strip())
    return last_read

def save_last_tweet(last_read, id):
    with open(id, 'w') as f_write:
        f_write.write(str(last_read))
    return

def reply_to_tweets(tweet_text):
    if 'pirop' in tweet_text:
        return random.choice(lista_respuestas.lista_piropos)
    elif 'opin' in tweet_text:
        return random.choice(lista_respuestas.lista_opiniones)
    elif '?' in tweet_text:
        return random.choice(lista_respuestas.lista_sino)
    else:
        return random.choice(lista_respuestas.lista_frases)
    
