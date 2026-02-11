from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the sportsmen website!")

def sports(request, sp_id):
    print(request.GET)
    return HttpResponse(f"<h1>Articles by sports</h1><p>Sports ID: {sp_id}</p>")

from django.http import HttpResponse, HttpResponseNotFound

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>404 - Page Not Found</h1>")