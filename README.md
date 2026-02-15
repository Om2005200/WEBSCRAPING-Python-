# WEBSCRAPING-Python-
This is the scrapping of stock market data from NSE website .
Here we will focus on the srapping of NSE market datas the methods I will be following here can be used to scrap various datas on 'NSE' sites this can solve many issues like keeping histortical datas etc.
I will be mainly floowing the most common method and reliable method tonscrap the websites is using the api endpoints .

NSE links to be used here :

[A] HISTORICAL INDEX DATA='https://www.nseindia.com/reports-indices-historical-index-data'
[B] FII/DII DATA='https://www.nseindia.com/reports/fii-dii'


There can bve several endpoints used to access datas based on the type of datas and analysis here I will be only showing how to access the historical index data and fii/dii data . First in order acess the always use the link1 as the webpage link the link of NSE webspage='https://www.nseindia.com/reports-indices-historical-index-data' this is the link you will get after you acess the historical index data then go to the centre of the page and right click at any place click inspect then go to the networks optins there it may show reload page options click it the page will be realoaded now selct the index and selct the timeframe of data you want to get here I have selected NIFTY 50 1D daily data after clciking these optins you will notice that in the networks tab a json will be upadted well there can be several jsons but check indiviually wit their reponses the moment u find the right endpoint go to the link you will get this api endpoint='/api/historicalOR/indicesHistory?indexType=NIFTY%2050&from=11-02-2026&to=12-02-2026' ['This is an example how the endpoints look']

Here I will aslo discuss hwow to save the json response into a json file and then convert the json file into a csv file. I have discussed the scrapping of two datasets i.e one is the scrapping of NIFTY 50 and the other is the FII/DII data here I have properly wrote the code in such a way that the the json responses can be directly saved into a json file and then converted into csv.

