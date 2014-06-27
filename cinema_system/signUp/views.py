from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages


def home(request):

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, "Welcome to the system!")
        return HttpResponseRedirect('/thankYou/')

    return render(request, 'signUp.html', locals())


def thankYou(request):

    return render(request, 'thankYou.html', locals())
