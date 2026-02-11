from django.urls import path
#from . import views  # 导入当前应用的views
from sportsmen.views import index, sports

#直接把所有应用的URL都放在主 urls.py 中不是好方法。我们应该为每个应用创建自己的 urls.py

urlpatterns = [
    path('', index),          # 对应 /sportsmen/
    path('sports/<int:sp_id>/', sports)   # 对应 /sportsmen/sports/
]