from django import forms
from .models import User
from django.forms import ModelForm


class RegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password1 = forms.CharField(label='Verify Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')

        if password != password1:
            raise forms.ValidationError(
                ("The two password fields didn't match.")
            )

        return cleaned_data

    def save(self):
        instance = super(RegistrationForm, self).save(commit=False)
        password = self.cleaned_data.get('password')

        instance.set_password(password)
        instance.save()
        return instance
