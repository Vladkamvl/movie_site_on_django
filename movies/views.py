from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Movie


class MoviesView(View):
    """Список фильмов"""
    @staticmethod
    def get(request):
        movies = Movie.objects.all()
        context = {
            'movies': movies,
        }
        return render(request, 'movies/movies.html', context)


class MovieDetail(View):
    """Деталка для фильма"""
    @staticmethod
    def get(request, pk):
        movie = Movie.objects.get(id=pk)
        context = {
            'movie': movie,
        }
        return render(request, 'movies/moviesingle.html', context)
