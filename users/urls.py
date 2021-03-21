from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url,include
from . import views


urlpatterns = [
    
      #url('^', include('django.contrib.auth.urls')),
      path("register/", views.register_request, name="register"),
      path("login/", views.login_request, name="login"),
      path("logout/", views.logout_request, name= "logout"),
]

