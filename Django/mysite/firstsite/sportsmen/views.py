from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the sportsmen website!")

def sports(request, year):
    return HttpResponse(f"<h1>Articles by sports</h1><p>Sports ID: {year}</p>")