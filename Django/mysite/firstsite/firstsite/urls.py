"""
URL configuration for firstsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings                 # 导入 settings
from django.conf.urls.static import static      # 导入 static
#from sportsmen.views import index, sports   #从 sportsmen 应用的 views.py 文件中导入 index 和 sports 这两个视图函数
#因为我们现在使用 include('sportsmen.urls')，URL 路由的责任已经转移给 sportsmen/urls.py
#sportsmen/urls.py 会自己导入需要的视图函数
from sportsmen.views import pageNotFound

#修改主 urls.py 使用 include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('sportsmen/', index),
    #这个路由现在由 sportsmen/urls.py 来管理
    #在 sportsmen/urls.py 中，我们有 path('', views.index) 来处理这个请求
    #include('sportsmen.urls') 会自动处理所有以 sportsmen/ 开头的 URL


    #path('sports/', sports)  #当用户访问 http://127.0.0.1:8000/sports/ 时，调用 sports 视图函数
    #这个路由已经移到 sportsmen/urls.py 中：path('sports/', views.sports)

    path('', include('sportsmen.urls')),  # 这里使用了 include 包含应用的urls
    #http://127.0.0.1:8000/sportsmen/sports/
]

# 设置 404
handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)