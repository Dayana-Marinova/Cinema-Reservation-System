from django import forms
from film.models import Film


class CatalogForm(forms.Form):
    CHOICES = (
        ('comedy', 'comedy'),
        ('thriller', 'thriller'),
        ('romantic', 'romantic'),
        ('animation', 'animation'),
        ('drama', 'drama'),
        ('criminal', 'criminal'),
        ('historical', 'historical'),
        ('documentary', 'documentary')
    )

    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICES)

    def search(self):
        categories = self.cleaned_data.get("categories")
        films = Film.objects.filter(category__in=categories)

        return films
