from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.player_list, name='player_list'),
    path('trainers/', views.trainer_list, name='trainer_list'),
]