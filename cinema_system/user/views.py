from django.shortcuts import render, redirect
from user.forms import RegistrationForm
from django.contrib.auth import views


def userRegiteration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thankYouRegister/')
    else:
        form = RegistrationForm()

        return render(request, "register.html", locals())


def thankYouRegister(request):

    return render(request, 'thankYouRegister.html', locals())


def login(request):
    if request.user.is_authenticated():
        return redirect('profile')
    else:
        return views.login(request, template_name='login_form.html')


def logout(request):
    views.logout(request)
    return redirect('/')
