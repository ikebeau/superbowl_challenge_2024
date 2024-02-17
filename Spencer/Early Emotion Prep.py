#%%
import pandas as pd


tw = pd.read_csv('C:/Users/spenc/Downloads/Final Keywords_2024.csv')

emojis = pd.read_csv('https://gist.githubusercontent.com/bfeldman89/fb25ddb63bdaa6de6ab7ac946acde96f/raw/8ae0f61016c5e5afb882a092de992e162ff4a907/emojis.csv',
                     on_bad_lines='skip',
                     names=['Emoji','Caption'])

#%%

tw['text_no_emojis'] = tw['text']
emojis2 = emojis.to_dict()
for i in range(len(emojis2['Emoji'])):
    tw['text_no_emojis'] = tw['text_no_emojis'].str.replace(emojis2['Emoji'][i],emojis2['Caption'][i])

#%%
import arrow as ar
tw.to_parquet('Tweets.parquet')
