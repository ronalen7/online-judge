from django.urls import path
from . import views

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index')
    path('', views.Index, name='index'),
    path('<int:problem_id>/', views.Detail, name='detail'),
]
