from django.urls import path

from . import views

urlpatterns = [
    path('', views.quizemail, name='index'),
    path('test/', views.test, name='test'),
]