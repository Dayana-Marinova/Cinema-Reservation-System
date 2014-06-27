from django.forms import ModelForm
from .models import Reservation


class ReservationForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.film = kwargs.pop('film')
        print(kwargs)
        super(ReservationForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        instance = super(ReservationForm, self).save(commit=False)
        instance.user = self.user
        instance.film = self.film
        instance.save(*args, **kwargs)
        return instance

    class Meta:
        model = Reservation
        exclude = ('user', 'film')
