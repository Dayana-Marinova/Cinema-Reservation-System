from django.shortcuts import render, HttpResponseRedirect, Http404, HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from user.models import User


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


def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        user = User.objects.get(username=request.POST['username'])
        if user.password == request.POST['password']:
            request.session['username_id'] = user.id
            return HttpResponseRedirect('/thankYou/')
    except user.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")


def logout(request):
    try:
        del request.session['username_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
