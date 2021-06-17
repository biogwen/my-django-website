from django.shortcuts import render
from .form import Email


def quizemail(request):
    form = Email()
    error = ""
    if request.method == 'POST':
        form = Email(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            domain_list = ["google.com"]
            domain = email.split('@')[1]
            if domain in domain_list:
                error = "Please put a professional email address"
            else:
                form.save()
                quizform()

    context = {'form': form, "error": error}

    return render(request, 'quizemail.html', context)


def test(request):
    form = Email()
    error = ""
    context = {'form': form, "error": error}

    return render(request, 'test.html', context)

# Create your views here.
