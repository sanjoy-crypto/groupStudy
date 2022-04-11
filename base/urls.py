from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('room/<str:pk>/',room,name="room"),
]
