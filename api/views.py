from django.shortcuts import render
from rest_framework import generics
from .models import Cv
from .serializer import CvSerializer

class ListCv(generics.ListAPIView):
    queryset = Cv.objects.all()
    serializer_class = CvSerializer