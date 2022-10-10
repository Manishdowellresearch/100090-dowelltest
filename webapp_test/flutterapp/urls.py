from django.urls import path

from flutterapp.views import details

urlpatterns =[
    path('details/',details, name= 'details'),
]