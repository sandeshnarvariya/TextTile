"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views   # import views file whom we made it.

urlpatterns = [
    path('admin', admin.site.urls),
    # Views file in present Index funtion callled
    path('', views.index, name='index'),
    # About is second funtion that type we are called about in views fill
    path('about', views.about, name='about'),

    path('analyze', views.analyze, name='analyze'),
    

]