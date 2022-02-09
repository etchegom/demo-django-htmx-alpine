from django import forms


MEDIA_TYPE_CHOICES = (
    ("Movie", "movie"),
    ("Serie", "series"),
    ("Episode", "episode"),
)


class MovieSearchForm(forms.Form):
    search = forms.CharField()
    media_type = forms.ChoiceField(required=True, choices=MEDIA_TYPE_CHOICES)
