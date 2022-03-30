from .models import Film, FilmDetail, FilmMain, FilmDate
from django.forms import ModelForm, DateInput
from django import forms
from django.core.validators import MinValueValidator


class FilmDetailForm(ModelForm):
    class Meta:
        model = FilmDetail
        exclude = ('film', )

    def __init__(self, *args, **kwargs):
        super(FilmDetailForm, self).__init__(*args, **kwargs)
        self.fields['country'].required = False
        self.fields['premiere'].required = False
        # self.fields['time'].required = False
        self.fields['director'].required = False
        self.fields['title'].required = False

class FilmMainForm(ModelForm):
    class Meta:
        model = FilmMain
        exclude = ('film', )

    def __init__(self, *args, **kwargs):
        super(FilmMainForm, self).__init__(*args, **kwargs)
        self.fields['genre'].required = False

class FilmDateForm(ModelForm):
    class Meta:
        model = FilmDate
        exclude = ('film', )

    def __init__(self, *args, **kwargs):
        super(FilmDateForm, self).__init__(*args, **kwargs)
        self.fields['day'].required = False
        self.fields['hour'].required = False

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['main', 'detail', 'date']

