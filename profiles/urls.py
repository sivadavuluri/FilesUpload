from django.urls import path
from .views import *
urlpatterns = [
    path('',Index,name='index'),
    path('profile/',Upload_Profile,name='profile'),
    path('search/',Search_Profile,name='search'),
]