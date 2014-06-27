from django.shortcuts import render
from .forms import CatalogForm


def catalogAll(request):
    data = request.POST if request.POST else None
    form = CatalogForm(data)

    if request.method == 'POST':
        if form.is_valid():
            films = form.search()
    
    return render(request, "catalog.html", locals())
