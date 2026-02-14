import requests as rq
import pandas as pd
import json
import os
url1='https://www.nseindia.com/reports/fii-dii'
url2='https://www.nseindia.com/api/fiidiiTradeReact'

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
session=rq.Session()
response1=session.get(url1,headers=main_headers)
print(response1.status_code)
response2=session.get(url2,headers=main_headers)
print(response2.status_code)
json_data=response2.json()
print(json_data)
def writing_data_to_json(path='demo_scrapping_fii_dii.json'):
  if os.path_exists(path):
    with open(path,'r') as x:
      l=json.load(x)
  else:
    l={}
  with open(path,'w') as y:
    json.dump(l,y,indent=4)
  return l

def converting_the_json_into_csv(path='fii_dii.csv'):
  with open('demo_scrapping_fii-dii.json','r') as t:
    data=json.load(t)
  result=pd.json_normalize(json_data['data'])
  
