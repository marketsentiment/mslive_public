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

This is program that creates the live sentiment charts. I had envisioned creating a realtime sentiment tracker so as to help me in trading. The hypothesis was by the time news is news, its already too late to sell/buy a stock. Wanted to gain an edge using this. Its still WIP. Please run the twitter and reddit stream atleast for half a day before triggering this code to get meaningful results. The dash part of the code is modified version of Sendex code from [here](https://github.com/Sentdex/socialsentiment). I have kept some parts that is not needed for the code since removing it causes the graph to crash. Not an expert in dash. You can improve upon this code the most. 

![Graph created from the program](https://user-images.githubusercontent.com/77964857/109548469-b149a500-7af2-11eb-87a2-349eb5ff2fca.png)


### reddit_stream.py

This is used to stream posts and comments from reddit in real-time. If your only aim is to identify growing stocks, you dont need to stream the data. You have lots of other ways around this. Streaming comments from reddit is not required as both pushshift and praw api gives historical data but since I am already streaming data from tweepy in my VM and using it for my live graph, I thought this was the best way to go. feel free to change this. Also WSB overpowers the rest of the subreddit in terms of comment volume. Feel free to play around with different subreddits which gives you the best results. 

### twitter_stream.py

Tweepy (Twitter API) does not allow free access to tweets more than 7 days old. Even if the tweets are within 7 days, there is a cap of 500K tweets per month for historical analysis. The program easily pulls around 100-150K tweets per day. So it's better to stream the tweets unless you have the premium version of the API. Read up on the rate limits and its impact before trying to stream the data. Also please note Tweepy will time you out for years if you keep hitting their server after you get a error. Its exponential and you can read up about experiences of other developers facing this same issue.  


### Ticker_count 

This is my quick and dirty version of counting the number of mentions of a ticker from the data that we stored. You have to run this code by specifying the time frame in which you want the analysis to be done. I have separated  both the twitter and reddit counts have been separated  as lots of people wanted the information to be separated in my subreddit. Feel free to combine them into one program. Do this for two-three months and you will have a good dataset to see how the mentions rise and fall based on the hype. Currently, I am running the code everyday at a fixed time and adding it to my excel tracker. If you have a better method, please feel free to suggest! 


### QC and final thoughts 
Obviously, just getting the number of mentions and their increase is just the first step. Two things that I am not sharing in the public repo is my own proprietary vadersentiment model (for finance related terms) and bot/spam detection. Please take a random sample and check whether the interest is genuine or whether the stocks are being pushed by bots (check for repeated mentions, very high comment/tweet volume from one user etc.) Also do your own extensive research before investing on any stocks. 


_Disclaimer: I am not a financial advisor. There are significant risks associated with investing in equities. Please do your own extensive research before investing in any stock._

