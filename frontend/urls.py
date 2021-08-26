from django.urls import path
from .views import index

app_name='frontend' #django needs to know this urls.py file belongs to the frontend app 
#this is the main urls
urlpatterns = [
    path('',index,name=''), # we don't have an way of identifying this paths so we give a formal name here 
    path('join',index),  
    path('create',index),
    path('room/<str:roomCode>', index)  
]   