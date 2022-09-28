from dataclasses import field
from itertools import product
import json
import requests
import pprint
from population import targeted_population
from connections import connection , github

#print(targeted_population('hr_hiring','product', ['projects_details'],"life_time"))

function_number =[
    '100001', '100002', '100003', '100004', '100005', '100006', '100007', '100008', '100009','100010',
    '100011', '100012', '100013', '100014', '100015', '100016', '100017', '100018', '100019', '100020', 
    '100021', '100022', '100023', '100024', '100025', '100026', '100027', '100028', '100029', '100030', 
    '100031', '100032', '100033', '100034', '100035', '100036', '100037', '100038', '100039','100040', 
    '100041', '100042', '100043', '100044', '100045', '100046', '100047', '100048', '100049', '100050', 
    '100051', '100053', '100054', '100055', '100056', '100057', '100058', '100059', '100060', 
    '100061', '100062', '100063', '100064', '100065', '100066', '100067', '100068', '100069', '100070', 
    '100071', '100072', '100073', '100074', '100075', '100076', '100077', '100078', '100079', '100080', 
    '100081', '100082', '100083', '100084', '100085', '100086', '100087', '100088', '100089', '100090', 
    '100091'
]
function_name = [
    'Data collection on cities','dowellconnection','dowelleventcreation' ,'dowellstattricks','dowellpixel',
    'dowellvideocompare','dowellautomatedpost','dowellglobaleventlist','dowellclock','dowellerror',
    'dowelltrackmyip','dowelllanguagedetection','dowellsamplequotacontrol','dowelllogin','dowellimputation',
    'dowellfaceid','dowellobjects','dowellworkfllow','dowellgeolocation','dowellquestiongenerator',
    'dowell5w5y','dowellrandomgraph','dowellnormality test','dowellsearchtrendln','dowellnpsdata',
    'dowellevents','dowellresearchsg','uxlivinglabcom','dowellshopify','dowellAI',
    'dowellsampling','dowelltargetedpopulation' ,'dowellsegmentation /dowellclassification function','dowellrecordingchannel function','dowellscale function',
    'dowellqualifyingsample','dowellsamplingrules function','dowelldistribution function','dowellclient reports','dowellautocomplete',
    'dowellreports ','dowellwebpagecompare','dowellexhibitorlist','dowellvendorregistration','dowellgithubbackup',
    'dowellchisqtest','dowellscaleconversion','dowellfeedback','dowellreportmodelling','dowellpermutation',
    'dowellcorrelation','dowelldataexport','dowellvoiceapp','dowellHRhiring','dowellqrcodegenerator',
    'dowelltaskestimator','dowelleditor','qrcodequeue','dowelltestingscenerios','dowellclassification',
    'dowellfindme','dowellmegaretrieve','dowellcomments','dowellsalesagent','dowellsentencecreation',
    'dowelleventreport','dowelllicenses','dowellchat','dowellinscribe function','dowelloverlapping shapes',
    'dowellshuffle','dowellqrcode','dowelllocation','dowelltraining','dowellvocnps',
    'dowellvocstories','dowellvocfeedback','dowellclientadmin','dowelllegalzard','community@uxlivinglab',
    'dowellplatformmanager','dowellconnection V2','workflow ai V2','dowellmailapi','dowellmap',
    'dowelllegalpractice','dowellpayment','dowellstore','dowelltest','dowellLogoscan'
    ]

"""a= len(function_number)
b= len(function_name)
for i in range(0,90):
    product_details= {
        "function_number":function_number[i],
        "function_name":function_name[i]
    }
"""
    #print(github(product_details))

#print(targeted_population('login','login',['Username'],'life_time'))

#print(github())
