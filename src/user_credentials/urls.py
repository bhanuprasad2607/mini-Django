"""user_credentials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

The URLs provided in accounts include django.contrib.auth.urls are:
    1. accounts/login/[name = 'login']
    2.accounts/logout/ [name='logout']
    3.accounts/password_change/ [name='password_change']
    4.accounts/password_change/done/ [name='password_change_done']
    6.accounts/password_reset/ [name='password_reset']
    7.accounts/password_reset/done/ [name='password_reset_done']
    8.accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    9.accounts/reset/done/ [name='password_reset_complete']

The auth files always checks for 'registeration/login.html' address pattern  
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('accounts/',include('accounts.urls')),
    path('',include('viewer.urls')),
]
