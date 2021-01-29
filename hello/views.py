from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def dishant(request):
    return HttpResponse('hello dishant!')

def sanjay(request):
    return HttpResponse('hello Sanjay!')

def greet(request, name):
    return HttpResponse(f'hello,{name}')