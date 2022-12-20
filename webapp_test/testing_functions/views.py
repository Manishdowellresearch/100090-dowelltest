from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

from testing_functions.utils import *

@csrf_exempt
def insert(request):
    field = {
        "eventId":get_event_id,
        "test":"testing"
        }
    updated_field={"test":"testing"}
    insert=dowellconnection("hr_hiring","hr_hiring","dowelltraining","dowelltraining","1000554","ABCDE","insert",field,updated_field)
    return JsonResponse({"status":insert})