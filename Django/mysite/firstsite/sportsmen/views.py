from django.shortcuts import render, redirect
#from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponse, HttpResponsePermanentRedirect, Http404
from .models import *
from django.urls import reverse
#from .models import Sportsman, Sports

# Create your views here.

#menu = ['About', 'Add article', 'Contacts', 'Sign in']

menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'add_article'},
    {'title': 'Contacts', 'url_name': 'contact'},
    {'title': 'Sign in', 'url_name': 'login'},
]

def index(request):
    #return HttpResponse("Welcome to the sportsmen website!")
    #return render(request, template_name: '?')
    #return render(request, template_name='sportsmen/index.html')
    #return render(request, template_name='sportsmen/index.html', context={'title':'Main page'})
    #return render(request, template_name='sportsmen/index.html', context={'menu': menu, 'title': 'Main page'})
    posts = Sportsman.objects.all()
    sports = Sports.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'sports': sports,
        'sport_selected': 0,
    }
    return render(request, 'sportsmen/index.html', context=context)
    #return render(request, 'sportsmen/index.html', {'posts': posts, 'menu': menu, 'title': 'Main page'})

def about(request):
    #return render(request, template_name='sportsmen/about.html')
    #return render(request, template_name='sportsmen/about.html', context={'title':'About'})
    sports = Sports.objects.all()
    context = {
        'menu': menu,
        'title': 'About',
        'sports': sports,
        'sport_selected': 0,
    }
    return render(request, 'sportsmen/about.html', context=context)

def sports(request, sp_id=None, year=None):
    if sp_id:
        return HttpResponse(f"<h1>Articles by sports</h1><p>{sp_id}</p>")
    elif year:
        return HttpResponse(f"<h1>Articles by sports</h1><p>{year}</p>")
    else:
        return HttpResponse("<h1>Articles by sports</h1>")

def show_post(request, post_id):
    return HttpResponse(f"Show the post with id: {post_id}")

    
def contact(request):
    return HttpResponse("Contacts")

def addarticle(request):
    return HttpResponse("Add article")

def login(request):
    return HttpResponse("Log in")

def show_sport(request, sport_id):
    posts = Sportsman.objects.filter(sport_id=sport_id)
    sports = Sports.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Display by sport category',
        'sports': sports,
        'sport_selected': sport_id,
    }
    return render(request, 'sportsmen/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>404 - Page Not Found</h1>")