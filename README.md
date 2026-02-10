# WEBSCRAPING-Python-
This is the scrapping of stock market data from NSE website .
Here we will focus on the srapping of NSE market datas the methods I will be following here can be used to scrap various datas on 'NSE' sites this can solve many issues like keeping histortical datas etc.
i will be scrapping by two methods one is by accesing the endpoints the other is by session based which is by the use of JWT and auth bearer these are time-based acessing as the cookies used here will expire depending upon the api time limits whereas the most reliable method is by accessing the endpoints but this can be only done on selctive websites if you can't acess by the endpoints method then you can freely use the time based accessing but for that you have to manually change the cookies periodically thsese JWT are mostly valid only for 1 day not mkore than that I will be clearly explaining step by step how to acess both of the things.

NSE links to be used here :
HISTORICAL INDEX DATA='https://www.nseindia.com/reports-indices-historical-index-data'
FII/DII DATA='https://www.nseindia.com/reports/fii-dii'

