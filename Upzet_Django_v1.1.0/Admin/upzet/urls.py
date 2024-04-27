
from django.contrib import admin
from django.urls import path,include


from upzet import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(),name="dashboard"),
    path('calendar', views.Calendar.as_view(),name="calendar"),
    path('settings',views.Settings.as_view(),name='settings'),
    # Email
    path('email/',include('e_mail.urls')),
    # Pages
    path('pages/',include('pages.urls')),
    #Components
    path('components/',include('components.urls')),
    #Components
    path('layouts/',include('layout.urls')),
    
    # Authentication
    path('account/', include('allauth.urls')),
    #Custum change password done page redirect
    path('accounts/password/change/', login_required(views.MyPasswordChangeView.as_view()), name="account_change_password"),
    #Custum set password done page redirect
    path('accounts/password/set/', login_required(views.MyPasswordSetView.as_view()), name="account_set_password"),

]
