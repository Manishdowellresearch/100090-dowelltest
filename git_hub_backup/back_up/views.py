from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def index(request):
    return HttpResponse("Manish")
