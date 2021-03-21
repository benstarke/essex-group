from . import views
from django.urls import path
from blog.views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.PostList.as_view(), name='post_list'),
    path('blogs/<str:slug>/', views.PostDetail, name='post_detail'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
]
