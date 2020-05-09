from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(' <marquee--> <h1> Blod Home </h1> </marquee>')

def home(request):
    return HttpResponse('<h1> About </h1> ')
