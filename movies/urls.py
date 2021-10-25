from django.urls import path

from .views import MoviesView, MovieDetail

urlpatterns = [
    path('', MoviesView.as_view(), name='home'),
    path('movie/<slug:slug>', MovieDetail.as_view(), name='movie_detail')
]
