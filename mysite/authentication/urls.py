from django.http import HttpResponse
from django.urls import path
from . import views
app_name = 'authentication'

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('problems/logout/', views.Logout, name='logout'),
    path('home/', views.Home, name='home')
    # path('login/', views.Login, name='login')
]
