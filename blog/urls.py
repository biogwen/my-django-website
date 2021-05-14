from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('articles/<str:name>/', views.articles, name='articles')
]