from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv', views.cv, name='cv'),
    path('consultancy', views.consultancy, name='consultancy'),
    path('contact', views.contact, name='contact'),
    path('contactrecrutement', views.contact_recrutement, name='contact recrutment'),
    path('contactaudit', views.contact_audit, name='contact audit'),
    path('thanks', views.thanks, name='thanks')
]