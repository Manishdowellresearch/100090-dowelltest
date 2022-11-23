from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from function.dowellpopulationfunction import targeted_population
from django.views.decorators.csrf import csrf_exempt
import json
from .models import repoDetails
from .serializers import RepoSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@csrf_exempt
def index(request):
    if request.method == "POST":
        try:
            dbname = request.POST.get("dbname")
            collection= request.POST.get("collection")
            field= request.POST.get("fields")
            time_period = "life_time"
            fetched_data = targeted_population(dbname,collection,[field],time_period)
            return JsonResponse({
                "Data fetched from Population function":fetched_data
            }) 
        except:
            return JsonResponse({
              "Status" : "There is no data i guess !"  
            }) 
    return render(request,'report.html')

@csrf_exempt
def github(request):
    if request.method == "GET":
        return JsonResponse({
            "Status":"Method not allowed. Post data to url"
        })
    if request.method == "POST":
        repository_name = request.POST.get("repository_name")
        repository_url= request.POST.get("repository_url")
        return JsonResponse({
            "repository_name": repository_name,
            "repository_url" : repository_url
        }) 

@csrf_exempt
def tp(request):
    if request.method == "GET":
        time_period = "life_time"
        fetched_data = targeted_population("master_db","database_details",["Database_name"],time_period)
        return JsonResponse({
            "Status":fetched_data
        })
    else:
        return JsonResponse({
            "Status":"Method not allowed. Post data to url"
        })
        
@api_view(['GET', 'POST'])
def repository_backup(request):
    if request.method == 'GET':
        repository= repoDetails.objects.all()
        serializer = RepoSerializer(repository, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RepoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)