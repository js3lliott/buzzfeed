import schedule
import json
import pandas as pd
import requests
import urlopen


url = 'https://newsapi.org/v2/everything?sources=buzzfeed&apiKey=0934e20a24a64265b468e8c8b075f6ce'
internet_check_url = "https://google.ca"

# def wait_for_internet_conn():
#     while True:
#         try:
#             response = urlopen(internet_check_url, timeout=1)
#             return
#         except Exception as e:
#             pass

def job():
    day = 0
    print("Loading...")
    for i in range(7):
        response = requests.get(url).json()
        content = json.dumps(response, indent=4, sort_keys=True)

        data = json.loads(content)['articles']

        buzz_df = pd.DataFrame(data)

        buzz_df.drop(['author', 'publishedAt', 'source', 'url', 'urlToImage'], inplace=True, axis=1)

        buzz_df.to_csv(f'buzz_df_day{day}.csv')
        
        day += 1

schedule.every().day.at("09:00").do(job)

# while 1:
#     wait_for_internet_conn()

schedule.run_pending()
