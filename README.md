<img src="https://static.wikia.nocookie.net/logopedia/images/a/ab/BuzzFeed_2.svg/revision/latest?cb=20160404171003" width="200" height="200" class="left"> 

# BuzzFeed Headline Analysis

   This is a fun little project I built that takes top headlines from BuzzFeed, using the News.org API, collected over a period of time and attempts create new BuzzFeed-style headlines from a custom AI model! The project is broken down into a few different sections starting off with a dedicated data collection notebook, then a notebook containing the code to merge all of the collected data files, a headline analysis notebook and lastly a notebook for our NLP models.

Click the links to skip right to where you want to go!
- [Data Collection](https://github.com/js3lliott/buzzfeed/blob/main/nbs/data_collection.ipynb)
- [Merging](https://github.com/js3lliott/buzzfeed/blob/main/nbs/data_concatenation.ipynb)
- [Exploratory Data Analysis](https://nbviewer.org/github/js3lliott/buzzfeed/blob/main/nbs/headline_eda.ipynb)
- [NLP Model]()

## Data Collection & Merging 💻

   To collect the headlines from BuzzFeed, I built a simple web scraper that utilized the [newsapi.org](https://newsapi.org/) API, the `requests` and `json` python libraries. The initial plan was to create a script that automated the scraping everyday but I had some trouble figuring it out so I manually ran the scraper which works just fine. Once I saved all of the csv files, I created a new notebook that loaded in the files via `glob` and just concatenated all of them together. 

## EDA 📊 

   Here is where we get into the weeds of exploring the text in-depth and try to extrapolate what parts come together to make BuzzFeed headlines as attractive and as attention-grabbing as they are. Starting with text analytics we visualize some basic statistics such as average word and title length, how many titles have numbers in them vs how many don't, which words are most commonly used, etc. The `WordCloud` library comes in handy to view the entire corpus of headlines. `Scikit-learn` also proved to be useful for creating n-grams with `CountVectorizer()`. Once I got some basic understanding of what the headines were made of, I moved on to some NLP analysis that included the use of `TextBlob` & `nltk` for sentiment analysis and `SpaCy` for visualizing Named Entity Recognition.

## NLP Model 📖