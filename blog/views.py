from django.shortcuts import render
from django.http import HttpResponse

def blog_index(request):
    return render(request, 'blog.html')

def articles(request, name):
    return render(request, 'article.html')