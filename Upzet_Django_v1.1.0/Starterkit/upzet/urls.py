"""upzet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include

from upzet import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(),name="dashboard"),
    
    # Pages
    path('pages/',include('pages.urls')),
    
    #Components
    path('layouts/',include('layout.urls')),
    
    # Authentication
    path('account/', include('allauth.urls')),
    #Custum change password done page redirect
    path('accounts/password/change/', login_required(views.MyPasswordChangeView.as_view()), name="account_change_password"),
    #Custum set password done page redirect
    path('accounts/password/set/', login_required(views.MyPasswordSetView.as_view()), name="account_set_password"),

]
