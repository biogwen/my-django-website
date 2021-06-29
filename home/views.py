from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .mailing import mailing

def index(request):

    return render(request, 'welcome.html')

def cv(request):
    args = {}
    datum = datetime.now()
    years = datum.year - 2007
    args['years'] = years
    return render(request, 'cv.html', args)

def consultancy(request):
    return render(request, 'consultancy.html')