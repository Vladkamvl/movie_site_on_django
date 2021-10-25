from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import DetailView

from .models import Movie


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(is_published=True)
    context_object_name = 'movies'
    template_name = 'movies/movies.html'


class MovieDetail(DetailView):
    """Деталка для фильма"""
    model = Movie
    slug_field = 'slug'
    template_name = 'movies/movie_detail.html'
