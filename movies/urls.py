from django.urls import path

from .views import MoviesView, MovieDetail

urlpatterns = [
    path('', MoviesView.as_view()),
    path('/movie/<int:pk>', MovieDetail.as_view())
]
