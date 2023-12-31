from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_request, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
]