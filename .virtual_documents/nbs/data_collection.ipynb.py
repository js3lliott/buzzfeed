import pandas as pd
import requests
import json


url = 'https://newsapi.org/v2/everything?sources=buzzfeed&apiKey=0934e20a24a64265b468e8c8b075f6ce'
response = requests.get(url).json()
content = json.dumps(response, indent=4, sort_keys=True)
print(content)


data = json.loads(content)['articles']

buzz_df = pd.DataFrame(data)
buzz_df.head()


buzz_df.drop(['author', 'publishedAt', 'source', 'url', 'urlToImage'], inplace=True, axis=1)


print(buzz_df.shape)
buzz_df.head()


buzz_df.to_csv('buzz_df_day2.csv')


get_ipython().getoutput("mv buzz_df_day2.csv ../data/")



