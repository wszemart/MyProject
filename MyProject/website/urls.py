from django.contrib import admin
from django.urls import path, include
from .views import main_view, film_view

urlpatterns = [
    path('', main_view, name = "main"),
    path('<int:pk>', film_view, name = "film")
]