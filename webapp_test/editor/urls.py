from django.urls import path

from editor.views import editor, editor_load ,index ,get_link

urlpatterns =[
    path('index/',index, name= 'index'),
    path('editor/',editor, name= 'editor'),
    path('editor_load/',editor_load, name= 'editor_load'),
    path('get_link/',get_link, name= 'get_link'),
]