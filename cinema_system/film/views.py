from django.shortcuts import render
from film.models import Film


def FilmAll(request):
    films = Film.objects.all()

    return render(request, "filmsall.html", locals())


def DescriptionFilm(request, filmtitle):
    film = Film.objects.get(title=filmtitle)

    return render(request, "singlefilm.thml", locals())
