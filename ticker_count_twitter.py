import mysql.connector
import pandas as pd

## Connect to mysql server 
mydb = mysql.connector.connect(
host ="",
user ="",
passwd = ""
)

mycursor = mydb.cursor()
df = pd.read_sql("select * from twitter_data.twitter_data_sentiment where date_time >= '2021-02-20 05:00:00' and date_time <= '2021-02-26 05:00:00'  ", mydb) ## Put in the time period of your analysis 
df_tickers = pd.read_csv('/home/nobjos/ticker_list_updated.csv') ## load list of tickers you want to analyze 
dollar_sign = "$"
output = pd.DataFrame({"ticker":['sample'], "count":[0],"dollar_count":[0],  "sentiment":[0]})

### There is multiple reasons why analysis is done in the following way 
# You have check the number of times a ticker is present - a ticker can be present either by just ticker or after a dollar sign. 
# Especially in reddit, in comments you very rarely see a dollar sign 
# why we are calcualting the dollar sign is not to have false positives 
# if there are a lot of mentions for the ticker but not succeeding a $ sign it might be false positive 
# A lot of comments and tweets will only have zero sentiment which will pull down the average - so remove the zero sentiment data before calculating the sentiment 

for ticker in df_tickers['Ticker']:
    a = df['tweet'].str.contains(" " + ticker + " ", case=False).sum()
    b = df['tweet'].str.contains(dollar_sign + ticker + " ", case=False, regex=False).sum()
    c = df[(df['tweet'].str.contains(" " + ticker + " ", case=False)) & (df['sentiment'] !=0)]['sentiment'].mean()
    df_one_ticker = pd.DataFrame({"ticker":[ticker], "count":[a], "dollar_count":[b], "sentiment":[c]})
    output = output.append(df_one_ticker)


output.to_csv('/home/nobjos/feb20_26_twitter_count.csv') ##location where you want the analysis output to be stored 

