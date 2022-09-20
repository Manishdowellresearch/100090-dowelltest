#dowellconnectionfunction
import json
import requests
import pprint
from datetime import datetime

def get_event_id():
    global event_id
    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    url="https://100003.pythonanywhere.com/event_creation"

    data={
        "platformcode":"FB" ,
        "citycode":"101",
        "daycode":"0",
        "dbcode":"pfm" ,
        "ip_address":"192.168.0.41",
        "login_id":"lav",
        "session_id":"new",
        "processcode":"1",
        "regional_time":time,
        "dowell_time":time,
        "location":"22446576",
        "objectcode":"1",
        "instancecode":"100051",
        "context":"afdafa ",
        "document_id":"3004",
        "rules":"some rules",
        "status":"work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour":"color value",
        "hashtags":"hash tag alue",
        "mentions":"mentions value",
        "emojis":"emojis",

    }


    r=requests.post(url,json=data)
    return r.text  
    
def connection(name):
    url = "http://100002.pythonanywhere.com/" 
    #searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"
    payload = json.dumps({
        "cluster": "hr_hiring",
        "database": "hr_hiring",
        "collection": "dowelltraining",
        "document": "dowelltraining",
        "team_member_ID": "1000554",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {
            "eventId" : get_event_id(),
            "full_name": name
            },
        "update_field": {
            "order_nos": 21
            },
        "platform": "bangalore"
        })
    headers = {
        'Content-Type': 'application/json'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


#63199b4e585165ea7d4efef2
#63199b99585165ea7d4eff02

"""
{"isSuccess": true, "inserted_id": "6320260837707385c6b162fd"}

{'_id': '6320260837707385c6b162fd', 'eventId': 'FB1010000000166305126257480583', 'full_name': 'chat', 'last_name': 'subproduct'}

{'_id': '6320260837707385c6b162fd', 'eventId': 'FB1010000000166305126257480583', 'full_name': 'bicky', 'last_name': 'subproduct'}

"""