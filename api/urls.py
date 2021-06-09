from django.urls import path

from .views import ListCv, Doc

urlpatterns = [
    path('', Doc, name='doc'),
    path('cv', ListCv.as_view(), name="CV"),

]