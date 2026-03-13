#from django.urls import path
from django.urls import path, re_path  # 导入re_path
#from . import views  # 导入当前应用的views
from sportsmen.views import index, sports, about
from sportsmen import views

#直接把所有应用的URL都放在主 urls.py 中不是好方法。我们应该为每个应用创建自己的 urls.py

urlpatterns = [
    path('addarticle/', views.addarticle, name='add_article'),
    
    #path('', index),          # 对应 /sportsmen/
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('sport/<slug:sport_slug>/', views.show_sport, name='sport'),
    
    #path('post/<int:post_id>/', views.show_post, name='post'),
    path('', index, name='home'), 
    path('sports/<int:sp_id>/', sports),
    path('sports/', sports),   # 对应 /sportsmen/sports/
    re_path(r'^sports/(?P<year>[0-9]{4})/$', sports),
    path('about/', about, name='about')
]