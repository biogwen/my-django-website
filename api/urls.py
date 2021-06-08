from django.urls import path

from .views import ListCv

urlpatterns = [
    path('', ListCv.as_view(), name="CV"),

]