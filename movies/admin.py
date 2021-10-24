from django.contrib import admin
from .models import Category, People, Genre, Movie, \
                    MovieShot, Rating, RatingStar, Reviews


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(People)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShot)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)



