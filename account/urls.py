from django.urls import path, include
from django.contrib.auth import views as autuh_views
from . import views

urlpatterns = [
    #path('login/', views.user_login, name='login')
    path("", views.dashboard, name='dashboard'),
    path('',include('django.contrib.auth.urls')),

    
]
