from django.urls import path

from testing_functions.views import *

urlpatterns =[
    path('insert/',insert, name= 'insert')
]