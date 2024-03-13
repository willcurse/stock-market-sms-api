import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

Stock_api_key="F7NBRER9BYPW2GAZ"
news_api_key="32c0c46ca445453588176c9f347f3509"

#twillio.....
account_sid= "AC175b190390ce444cbb005689139326a8"
auth_token="4b01dcee3a20fbbbaefd10d48d90b1fc"
twillio_number=+12176152565


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":Stock_api_key,
}

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

request=requests.get(STOCK_ENDPOINT,params=stock_params)
data=request.json()["Time Series (Daily)"]
#converting into list...
data_list=[value for (key,value) in data.items()]
yesterday=data_list[0]
y_closing_price=yesterday["4. close"]
print(y_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_y=data_list[1]
day_before_y_close_price=day_before_y["4. close"]
print(day_before_y_close_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference=abs(float(y_closing_price)-float(day_before_y_close_price))
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

difference_per=(difference/float(y_closing_price))*100
print(difference_per)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if difference_per<1:
    news_params={
        "apiKey":news_api_key,
        "qInTitle":COMPANY_NAME,
    }

 
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    article=news_response.json()["articles"]
    
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    one_article=article[:1]
    #print(one_article)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    
    formatted=[f"HeadLine:{article ['title']}. \nBrief: {article ['description']}"for article in one_article]
    print(formatted)
#TODO 9. - Send each article as a separate message via Twilio. 
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
         body=formatted,
         from_=twillio_number,
         to='+917895099154'
     )
print(message.sid)


