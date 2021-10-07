import pandas as pd
import requests
import json


url = ('https://newsapi.org/v2/everything?sources=buzzfeed&apiKey=0934e20a24a64265b468e8c8b075f6ce')
response = requests.get(url).json()
content = json.dumps(response, indent=4, sort_keys=True)
print(content)


buzz_list = []
data = json.loads(content)

for title in data["articles"]:
  buzz_list.append([title['content'], title['description'], title['title']])

buzz_df = pd.DataFrame(buzz_list)
buzz_df.head()


buzz_df.columns = ["content", "description", "title"]



print(buzz_df.shape)
buzz_df.head()


buzz_df.to_csv('buzz_df_day1.csv')


get_ipython().getoutput("mv buzz_df_day1.csv ../data/")



