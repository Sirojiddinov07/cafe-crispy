from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_view


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
    path('password_reset/', auth_view.PasswordResetView.as_view
    (template_name='password_reset.html'),
    name='password_reset'),
    path('password_reset_sent/', auth_view.PasswordResetDoneView.as_view(),
    name='password_reset_sent'),
    path('/reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm'),
    path('password_reset_complete', auth_view.PasswordResetCompleteView.as_view(),
    name='password_reset_complete'),

]
