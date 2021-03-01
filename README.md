# Market Sentiment 

### About 
This repository can mainly be used for two things. 

a. Tracking the live sentiment of stocks from Reddit and Twitter

b. Tracking the number of mentions for particular tickers in Reddit and Twitter

### config.py

Add the tickers and stock information about the companies that you want to track. This is for live sentiment and not for tracking the number of mentions 

### dev_server.py 

If you want to run the program (live tracker for sentiment) in your local machine, run via this 

### live_sentiment.py

This is program that creates the live sentiment charts. Please run the twitter and reddit stream atleast for half a day before triggering this code to get meaningful results. The dash part of the code is modified version of Sendex code from [here](https://github.com/Sentdex/socialsentiment). I have kept some parts that is not needed for the code since removing it causes the graph to crash. Not an expert in dash. You can improve upon this code the most. 
