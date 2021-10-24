from django.contrib import admin
from .models import Category, People, Genre, Movie, \
                    MovieShot, Rating, RatingStar, Reviews

admin.site.register(Category)
admin.site.register(People)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShot)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
