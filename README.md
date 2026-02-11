# WEBSCRAPING-Python-
This is the scrapping of stock market data from NSE website .
Here we will focus on the srapping of NSE market datas the methods I will be following here can be used to scrap various datas on 'NSE' sites this can solve many issues like keeping histortical datas etc.
i will be scrapping by two methods one is by accesing the endpoints the other is by session based which is by the use of JWT and auth bearer these are time-based acessing as the cookies used here will expire depending upon the api time limits whereas the most reliable method is by accessing the endpoints but this can be only done on selctive websites if you can't acess by the endpoints method then you can freely use the time based accessing but for that you have to manually change the cookies periodically thsese JWT are mostly valid only for 1 day not mkore than that I will be clearly explaining step by step how to acess both of the things.

NSE links to be used here :

[A] HISTORICAL INDEX DATA='https://www.nseindia.com/reports-indices-historical-index-data'
[B] FII/DII DATA='https://www.nseindia.com/reports/fii-dii'


There can bve several endpoints used to access datas based on the type of datas and analysis here I will be only showing how to access the historical index data and fii/dii data 


First in order acess the always use the link1 as the webpage link the link of NSE webspage='https://www.nseindia.com/reports-indices-historical-index-data' this is the link you will get after you acess the historical index data then go to the centre of the page and right click at any place click inspect then go to the networks optins there it may show reload page options click it the page will be realoaded now selct the index and selct the timeframe of data you want to get here I have selected NIFTY 50 1D daily data after clciking these optins you will notice that in the networks tab a json will be upadted well there can be several jsons but check indiviually wit their reponses the moment u find the right endpoint go to the link you will get this api endpoint='/api/historicalOR/indicesHistory?indexType=NIFTY%2050&from=11-02-2026&to=12-02-2026' 
Here I will aslo discuss hwow to save the json response into a json file and then convert the json file into a csv file.

