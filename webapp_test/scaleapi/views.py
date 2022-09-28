from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from function.dowellconnection import dowellconnection
from function.event import get_event_id
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def scale(request):
    if request.method == "POST":
        data= request.POST.get('data')
        a=type(data)
        return JsonResponse({
            "type":a,
            "data": data 
            })

@csrf_exempt
def scaleapi(request):
    if request.method == "POST":
        scale_data = request.POST.get('scale_data')
        scale=json.loads(scale_data)
        field ={
            "eventId":get_event_id(),
            "scale_data": scale
        }
        inserted_id= dowellconnection("dowellscale","dowellscale","scale_reports","scale_reports","1094","ABCDE","insert",field)
        return JsonResponse({
            "inserted_id": inserted_id,
            "status":"Inserted sucessfully" 
            })


