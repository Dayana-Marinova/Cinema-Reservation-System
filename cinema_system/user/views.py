from django.shortcuts import render
from django.http import HttpResponse
from user.forms import RegistrationForm


def UserRegiteration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponse('/thankYouRegister/')
    else:
        form = RegistrationForm()

        return render(request, "register.html", locals())


def thankYouRegister(request):

    return render(request, 'thankYouRegister.html', locals())
