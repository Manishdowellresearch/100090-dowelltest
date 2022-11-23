
from django.urls import path
from getReports.views import index,github ,tp ,repository_backup

urlpatterns = [
    path('index/',index, name= 'index'),
    path('github/',github, name= 'github'),
    path('tp/',tp, name= 'tp'),
    path('repository_backup/',repository_backup, name= 'repository_backup'),
]


