from django.urls import path

from scaleapi.views import scale ,scaleapi

urlpatterns =[
    path('scale/',scale, name= 'scale'),
    path('scaleapi/',scaleapi, name= 'scaleapi'),
]