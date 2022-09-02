import django
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('typography/', views.typography, name='typography'),
    path('contacts/', views.contacts, name='contacts'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:uname>', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
]