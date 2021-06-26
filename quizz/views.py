from django.shortcuts import render
from .form import PostForm, quizagile


def quizemail(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.save()
            request.session['email'] = email.email
            print(request.session.get('email'),)



    context = {'form': form}

    return render(request, 'quizemail.html', context)


def test(request):
    form = quizagile()
    error = ""
    context = {'form': form, "error": error}

    return render(request, 'test.html', context)

# Create your views here.
