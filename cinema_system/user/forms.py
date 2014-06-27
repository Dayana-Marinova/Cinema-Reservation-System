from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import User


class RegistrationForm(ModelForm):
    username = forms.CharField(label='Your name')
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label='Verify Password', widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('That username is allready taken, please select another.')

    def clean_password(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise forms.ValidationError('The passwords didn`t match. Please try again.')
        return password
