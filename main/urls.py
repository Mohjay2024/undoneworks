from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('principles/', views.principles, name='principles'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('articles/', views.articles, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
]