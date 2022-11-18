
from django.urls import path
from getReports.views import index,github ,tp

urlpatterns = [
    path('index/',index, name= 'index'),
    path('github/',github, name= 'github'),
    path('tp/',tp, name= 'tp'),
]