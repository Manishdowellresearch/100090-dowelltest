from django.urls import path

from back_up.views import index , repositoryClone ,webhookss

urlpatterns =[
  path('index/',index, name= 'index'),
  path('repositoryClone/',repositoryClone, name= 'repositoryClone'),
  path('dowell/<str:repo_name>/',webhookss, name= 'webhookss'),
  #path('task_report/',task_report, name= 'task_report'),
  #path('timeperiod/',timeperiod, name= 'timeperiod'),
  #path('hr_report/',hr_report, name= 'hr_report'),
  #path('mainpage/',mainpage, name= 'mainpage'),
  #path('Teamlead_report/',Teamlead_report, name= 'Teamlead_report'),
  
]