import snscrape.modules.twitter as sntwitter
import pandas as pd

attributes_container = []
users = ['@lusia_____'] # List of users to scrape tweets from

for u in users:
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{}'.format(u)).get_items()):
        if i>6000:
            break
        attributes_container.append([tweet.rawContent])
        
tweets_df = pd.DataFrame(attributes_container, columns =['tweets'])

# Cleaning data: dropping all tweets with links and mentions and adding 
# markers for GPT-2 to recognize the start and end of the tweets.
tweets_df = tweets_df[tweets_df['tweets'].str.contains('http|@') == False]
tweets_df = tweets_df['tweets'].apply(lambda x: '{}{}{}'.format('<|startoftext|>', x, '<|endoftext|>'))

print(tweets_df.head())

# Sending data to .csv file
file_name = 'tweets_no_mentions_complete.csv'
tweets_df.to_csv(file_name, encoding ='utf-8', index = False, header=False)