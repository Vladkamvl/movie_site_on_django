from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.views.generic import DetailView

from .models import Movie, Reviews
from .forms import ReviewForm

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


class AddReview(View):
    """Отзывы"""
    def post(self, request, movie_id):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent_id', False):
                form.parent_id = int(request.POST.get('parent_id'))
            form.movie_id = movie_id
            form.save()

        movie = Movie.objects.get(pk=movie_id)
        return redirect(movie)
