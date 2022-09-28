#dowellconnectionfunction
import json
import requests
import pprint
from datetime import datetime


url = "http://100002.pythonanywhere.com/" 
#searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"
payload = json.dumps({
    "cluster": "login",
    "database": "login",
    "collection": "registration",
    "document": "registration",
    "team_member_ID": "10004545",
    "function_ID": "ABCDE",
    "command": "find",
    "field": {
        "Username":"Shrinivas"
        },
    "platform": "bangalore"
    })
headers = {
    'Content-Type': 'application/json'
    }
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

