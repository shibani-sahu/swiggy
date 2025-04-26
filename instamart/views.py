from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chocolate(request):
    return HttpResponse("I alwaya eat chocolates")

def first(request):
    return render(request,'first.html')