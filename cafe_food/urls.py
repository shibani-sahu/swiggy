from django.urls import path
from cafe_food.views import *
app_name= 'cafe_food'
urlpatterns=[
path('B/', biriyani, name='biriyani'),
path('I/', icecream, name='icaecream'),
  

]





