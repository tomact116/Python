from django.urls import path
from . import views  # 导入当前应用的views

#直接把所有应用的URL都放在主 urls.py 中不是好方法。我们应该为每个应用创建自己的 urls.py

urlpatterns = [
    path('', views.index),          # 对应 /sportsmen/
    path('sports/', views.sports)   # 对应 /sportsmen/sports/
]