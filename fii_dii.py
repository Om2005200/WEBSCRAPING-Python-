import requests as rq                                                                                                                                       #importing the modeules
import pandas as pd
import json
import os

url1='https://www.nseindia.com/reports/fii-dii'                                                                                                              #api endpoints 
url2='https://www.nseindia.com/api/fiidiiTradeReact'

main_headers = {
    "Dnt": "1",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',                                                                                                                       #headers
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
session=rq.Session()                                                                                                                                         # creating a session
response1=session.get(url1,headers=main_headers)
print(response1.status_code)
response2=session.get(url2,headers=main_headers)
print(response2.status_code)
json_data=response2.json()
print(json_data)
def writing_data_to_json(path='demo_scrapping_fii_dii.json'):
  if os.path_exists(path):                                                                                                                                   # checks if the file exists or not
    with open(path,'r') as x:
      l=json.load(x)                                                                                                                                         # opens the file in read mode
  else:
    l=[]                                                                                                                                                     # empty list to append data
  l=json_data                                                                                                                                                # writes the json reposne2 into the json file not via api
  with open(path,'w') as y:
    json.dump(l,y,indent=4)                                                                                                                                  # saves the json data into the file
  return l

def converting_the_json_into_csv(path='fii_dii.csv'):
  with open('demo_scrapping_fii-dii.json','r') as t:                                                                                                         # opening the json file in which data is saved 
    data=json.load(t)
  result=pd.json_normalize(json_data)                                                                                                                         # normalizing the data
  result.rename(columns={                                                                                                                                     # renaming the raw columns (Optional)
        'category':'CATEGORY',    
        'date':'DATE',
        'buyValue':'BUY_VALUE',
        'sellValue':'SELL_VALUE',
        'netValue':''NET_VALUE'
    },inplace=True)
  result=result[['CATEGORY','DATE','BUY_VALUE','SELL_VALUE','NET_VALUE']]                                                                                     # arranging the column names 
  if os.path.exists(path):
      result.to_csv(path,mode='a',header=False,index=False)                                                                                                   # conditional statemnts to check if csv exists or not 
  else:
      result.to_csv(path,mode='w',header=False,index=False)
w=writing_data_to_json()
o=converting_the_json_into_csv()                                                                                                                              # calling the functions

    
  
