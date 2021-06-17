from django.shortcuts import render
from .form import PostForm


def quizemail(request):
    form = PostForm()
    error = ""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.save()

            domain_list = ["gmail.com",]
            email = email.email
            domain = email.split('@')
            domain = domain[1]
            print (domain)
            if domain in domain_list:
                error = "Please put a professional email address"
            else:
                error = ''

    context = {'form': form, "error": error}

    return render(request, 'quizemail.html', context)


def test(request):
    form = PostForm()
    error = ""
    context = {'form': form, "error": error}

    return render(request, 'test.html', context)

# Create your views here.
