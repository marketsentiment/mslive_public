#-*- coding: utf-8 -*- 
import pandas as pd 
## Add your stock tickers here which are required for live tracking 
## reason for both the ticker and name is to analyze the difference in sentiment and mentions betweent the ticker and company name
## some comapnies like Visa have a ticker $V which becomes difficult to efficiently track 
data_dict = {"Apple(AAPL)":["AAPL","Apple"],
"Microsoft(MSFT)":["MSFT","Microsoft"]
}
data_dict_df = pd.DataFrame(data_dict)


