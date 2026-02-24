from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect

# Create your views here.
from django.http import HttpResponse

menu = ['About', 'Add article', 'Contacts', 'Sign in']

def index(request):
    #return HttpResponse("Welcome to the sportsmen website!")
    #return render(request, template_name: '?')
    #return render(request, template_name='sportsmen/index.html')
    #return render(request, template_name='sportsmen/index.html', context={'title':'Main page'})
    return render(request, template_name='sportsmen/index.html', context={'menu': menu, 'title': 'Main page'})

def about(request):
    #return render(request, template_name='sportsmen/about.html')
    #return render(request, template_name='sportsmen/about.html', context={'title':'About'})
    return render(request, template_name='sportsmen/about.html', context={'menu': menu, 'title': 'About page'})

def sports(request, sp_id):
    if(request.GET):
        print(request.GET)

    if(sp_id>10):
        #raise Http404()
        #return redirect('/')
        #return redirect(to='/', permanent=True)
        return HttpResponsePermanentRedirect('/')


    return HttpResponse(f"<h1>Articles by sports</h1><p>Sports ID: {sp_id}</p>")



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>404 - Page Not Found</h1>")