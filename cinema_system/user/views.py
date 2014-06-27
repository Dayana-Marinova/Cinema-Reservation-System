from django.shortcuts import render
from django.http import HttpResponseRedirect
from user.forms import RegistrationForm
from .models import User


def UserRegiteration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.Objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            user = user.get_profile()
            return HttpResponseRedirect('/thankYouRegister/')
    else:
        form = RegistrationForm()

        return render(request, "register.html", locals())


def thankYouRegister(request):

    return render(request, 'thankYouRegister.html', locals())
