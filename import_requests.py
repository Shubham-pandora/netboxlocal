import site
from unicodedata import name
from unittest import result
import requests
import json

url = "http://192.168.0.108:8001/api/dcim/sites/"

headers = {
    'content-type': "application/json",
    'authorization': "Token c384a68ab0733a26c11b60ac0221180f10a86d1a",
    'cache-control': "no-cache",
    'postman-token': "356fdcce-4d66-a618-1d36-f44f4588d057"
    }

response = requests.request("GET", url, headers=headers)
json_data = response.json()
# print(response.text)
results = json_data['results']   #result is key , check get request
print(type(response))
print(type(json_data))
for sitename in results:
    siteurl = sitename['url']
    sitename = sitename['name']
    # name = sitename['name']
    # print(sitename)
    # print(sitename['display'])
    print('The API_URL of sitename :' + sitename + '  is : ' + siteurl)
    