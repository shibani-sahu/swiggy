from django.urls import path
from instamart.views import *
app_name='swiggy'
urlpatterns=[
    path('chocolate/', chocolate , name='chocolate'),
    path('first/', first , name='first'),
    

]