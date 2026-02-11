#from django.urls import path
from django.urls import path, re_path  # 导入re_path
#from . import views  # 导入当前应用的views
from sportsmen.views import index, sports

#直接把所有应用的URL都放在主 urls.py 中不是好方法。我们应该为每个应用创建自己的 urls.py

urlpatterns = [
    #path('', index),          # 对应 /sportsmen/
    path('', index, name='home'), 
    path('sports/<int:sp_id>/', sports)
    #path('sports/', sports)   # 对应 /sportsmen/sports/
    #re_path(r'^sports/(?P<year>[0-9]{4})/$', sports),
]