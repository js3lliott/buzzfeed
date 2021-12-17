<img src="https://static.wikia.nocookie.net/logopedia/images/a/ab/BuzzFeed_2.svg/revision/latest?cb=20160404171003" width="200" height="200" class="left"> 

# BuzzFeed Headline Analysis

This is a fun little project I built that takes top headlines from BuzzFeed, using the News.org API, collected over 20 days and attempts create new BuzzFeed-style headlines from a custom AI model! The project is broken down into a few different sections starting off with a dedicated data collection notebook, then a notebook containing the code to merge all of the collected data files, a headline analysis notebook and lastly a notebook for our NLP model.

Click the links to skip right to where you want to go!
- [Data Collection](https://github.com/js3lliott/buzzfeed/blob/main/nbs/data_collection.ipynb)
- [Merging](https://github.com/js3lliott/buzzfeed/blob/main/nbs/data_concatenation.ipynb)
- [Exploratory Data Analysis](https://nbviewer.org/github/js3lliott/buzzfeed/blob/main/nbs/headline_eda.ipynb)
- [NLP Model]()

## Data Collection & Merging 💻

To collect the headlines from BuzzFeed, I built a simple web scraper that utilized the [newsapi.org](https://newsapi.org/) API, the `requests` and `json` python libraries. The initial plan was to create a script that automated the scraping everyday but I couldn't quite figure that out so I manually ran the scraper for the 20 days of collection which worked just fine. Once I saved all of the csv files, I created a new notebook that loaded in the files via `glob` and just concatenated all of them together. 

## EDA 📊 

## NLP Model 📖