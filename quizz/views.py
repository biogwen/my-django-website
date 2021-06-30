from django.shortcuts import render, redirect
from .form import PostForm, Quizagile
from .logicquiz import logic
from django.core.mail import EmailMessage


def quizemail(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.save()
            request.session['email'] = email.email
            print(request.session.get('email'),)
            return redirect('test')



    context = {'form': form}

    return render(request, 'quizemail.html', context)


def test(request):
    form = Quizagile()
    if request.method == 'POST':
        form = Quizagile(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()

            request.session['methodology'] = logic(quiz.maturity, quiz.teamsize, quiz.company_size, quiz.sprint_time)

            return redirect('result')


    error = ""
    context = {'form': form, "error": error}

    return render(request, 'test.html', context)

# Create your views here.
def result(request):

    methodology = request.session.get('methodology')
    email = request.session.get('email')

    emailing = EmailMessage(
        "Test result",
        methodology,
        email,
        ['gwenael@mycoachingcompany.eu'],

        reply_to=[email],
        headers={'Message-ID': 'test result'},
    )
    emailing.send(fail_silently=False)
    context = {'methodology': methodology, 'email': email}
    return render(request, 'result.html', context)
    