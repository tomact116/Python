from django.shortcuts import render, redirect
#from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponse, HttpResponsePermanentRedirect, Http404
from .models import *
from django.urls import reverse
#from .models import Sportsman, Sports
from django.shortcuts import get_object_or_404
from .forms import AddArticleForm

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
    #sports = Sports.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        #'sports': sports,
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

def show_post(request, post_slug):
    post = get_object_or_404(Sportsman, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'sport_selected': post.sport_id,
    }
    return render(request, 'sportsmen/post.html', context=context)
    #return HttpResponse(f"Show the post with id: {post_id}")

    
def contact(request):
    return HttpResponse("Contacts")

def addarticle(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddArticleForm()
    return render(request, 'sportsmen/addarticle.html', {
        'menu': menu,
        'title': 'Add article',
        'form': form
    })

def login(request):
    return HttpResponse("Log in")

def show_sport(request, sport_slug):
    sport = get_object_or_404(Sports, slug=sport_slug)
    posts = Sportsman.objects.filter(sport_id=sport.id)
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Display by sport category',
        'sport_selected': sport.id,
    }
    return render(request, 'sportsmen/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>404 - Page Not Found</h1>")