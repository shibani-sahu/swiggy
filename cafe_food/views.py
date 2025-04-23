from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def biriyani(request):
    return HttpResponse("Biriyani is so tasty")

def icecream(request):
    return HttpResponse("Icecream is so cool")

