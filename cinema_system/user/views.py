from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from user.forms import RegistrationForm

def UserRegiteration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
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
	else:
		form = RegistrationForm()

		return render(request, "register.html", locals())