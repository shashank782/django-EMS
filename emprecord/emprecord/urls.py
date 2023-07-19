"""emprecord URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index' ),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile, name='profile'),
    path('logout/',views.Logout,name='logout'),
    #path('admin_login/',views.admin_login,name='admin_login'),
    path('my_experience/',views.my_experience,name='my_experience'),    
    path('edit_experience/',views.edit_experience,name='edit_experience'),
    path('my_education/',views.my_education,name='my_education'),    
    path('edit_education/',views.edit_education,name='edit_education'),
    path('change_password/',views.change_password,name='change_password'),
    #path('admin_home/',views.admin_home,name='admin_home'),




]
