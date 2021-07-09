from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError
from.form import PostForm

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


def contact(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            subject = "contact"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'gwenael@mycoachingcompany.eu', ['gwenael@mycoachingcompany.eu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')





    title = "Contact"
    context = {'form': form, "title": title}

    return render(request, 'contact.html', context)


def contact_recrutement(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            subject = "contact recrutement"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'gwenael@mycoachingcompany.eu', ['gwenael@mycoachingcompany.eu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')

    title = "More information"
    context = {'form': form, "title": title}
    return render(request, 'contact.html', context)


def contact_audit(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            subject = "contact audit"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'gwenael@mycoachingcompany.eu', ['gwenael@mycoachingcompany.eu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')

    title = "More information about the audits"
    context = {'form': form, "title": title}
    return render(request, 'contact.html', context)

def thanks(request):
    return render(request, 'Thanks.html')