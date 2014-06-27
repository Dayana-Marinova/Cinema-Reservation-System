from django.shortcuts import render, redirect
from film.models import Film
from .forms import ReservationForm


def filmAll(request):
    films = Film.objects.all()

    return render(request, "filmsall.html", locals())


def descriptionFilm(request, filmtitle):
    film = Film.objects.get(title=filmtitle)
    data = request.POST if request.POST else None
    form = ReservationForm(data, film=film, user=request.user)

    if request.method == 'POST' and request.user.is_authenticated:
        if form.is_valid():
            form.save()
            return redirect('/thankYouReservation/')

    return render(request, "singlefilm.html", locals())


def home(request):
    return render(request, "home.html", locals())
