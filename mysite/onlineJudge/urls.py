from django.urls import path
from . import views
app_name = 'onlineJudge'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index')
    path('', views.Index, name='index'),
    path('<int:problem_id>/', views.Detail, name='detail'),
    path('<int:problem_id>/submit/', views.submitProblem, name='submit'),
]
