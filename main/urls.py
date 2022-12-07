from django.urls import path
from .views import *


urlpatterns =[
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('news/', news, name='news'),
    path('reserve/', reserve, name='reserve'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logoutUser, name='logout'),
    path('news_detail/<int:pk>/', news_detail, name='news_detail'),
    path('food_detail/<int:pk>/', food_detail, name='food_detail'),
    path('team_detail/<int:pk>/', team_detail, name='team_detail'),
]
