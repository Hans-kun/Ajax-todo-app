from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # path('', views.home, name='home'),
    path('todo/', views.HomeView.as_view()),
    path('tododetail/<int:id>/', views.DetailView.as_view()),
]