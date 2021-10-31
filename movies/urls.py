from django.urls import path

from .views import MoviesView, MovieDetail, AddReview

urlpatterns = [
    path('', MoviesView.as_view(), name='home'),
    path('movie/<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('review/<int:movie_id>', AddReview.as_view(), name='add_review'),
]
