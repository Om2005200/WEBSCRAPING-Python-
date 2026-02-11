import requests as rq   # impoorting the request with aliasing as rq
import pamdas as pd     # importing the pnadas with aliasing as pd
import csv              # python's own csv module
import json             # java script oriented file that mainly recobverts the reponse into json 

url1='https://www.nseindia.com/reports-indices-historical-index-data'                                               
url2='https://www.nseindia.com/api/historicalOR/indicesHistory?indexType=NIFTY%2050&from=11-02-2026&to=12-02-2026'

main_headers = {
    "Dnt": "1",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

session=rq.Session()                                             #creating a session for the get resquest
response1=session.get(url1,headers=main_headers)
print(response.status_code)                                      # printing the status code this will give '200' for succesfull response else 404 or other HTTP Exceptions
response2=session.get(url2,headers=main_headers)
print(response.status_code)
json_data=response.json()                                                       # receiving the jso response 
print(json_data)
def writing_the_data_to_json(path='nifty_50_raw_data.json'):                    # function to create convert the json response into a temporary json file
  with open(path,'w') as x:
    l=json.dump(json_data,x,indent=4)                                           # convert the json response into json file
    return l
def converting_the_json_into_csv(path='nifty_50.csv'):                          # function to convert the json response into csv
  with open('demo_scrapping.json','r') as x:
    data=json.load(x)                                                           # this will load the json data so as to convert the data into csv
  result=pd.json_normalize(data['data'])                                        # data is a list of dicts inside which a list named as 'data' 
  result.to_csv(path,index=False)

e=writing_the_data_to_json()                                                     
g=converting_the_json_into_csv()



