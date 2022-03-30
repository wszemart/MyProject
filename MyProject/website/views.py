# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# # Create your views here.
# # request -> response
#
# def say_hello(request):
#     return render(request, 'hello.html')

from django.shortcuts import render

# Create your views here.
from film.forms import FilmForm, FilmDetailForm, FilmMainForm, FilmDateForm
from film.models import Film, FilmDetail, FilmMain, FilmDate

def main_view(request):
    context = {}
    template = "main.html"
    if request.method == 'GET':
        film_details_form = FilmDetailForm(prefix='detail')
        film_main_form = FilmMainForm(prefix='main')
        film_date_form = FilmDateForm(prefix='date')
        context["film_details_form"] = film_details_form
        context["film_main_form"] = film_main_form
        context["film_date_form"] = film_date_form
        return render(request, template, context)
    if request.method == "POST":
        films = Film.objects.select_related("main").select_related("detail").all()
        film_details_form = FilmDetailForm(request.POST, prefix='detail')
        film_main_form = FilmMainForm(request.POST, prefix='main')
        film_date_form = FilmDateForm(request.POST, prefix='date')
        if film_details_form.is_valid() and film_main_form.is_valid():
            genre = film_main_form.cleaned_data['genre']
            if genre:
                films = films.filter(main__genre=genre)


        context['films'] = films
        print(films)
        context["film_details_form"] = film_details_form
        context["film_main_form"] = film_main_form
        context["film_date_form"] = film_date_form
        return render(request, template, context)


def film_view(request, pk):
    template="film.html"
    context={}
    if request.method == "GET":
        film = Film.objects.get(id=pk)
        context['film'] = film
        return render(request, template, context)