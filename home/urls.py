from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv', views.cv, name='cv'),
    path('consultancy', views.consultancy, name='consultancy')
]