from django.db import models


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField("Категория", max_length=160)
    description = models.TextField("Описание")
    slug = models.SlugField("Слаг", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class People(models.Model):
    """Модель актёров/режиссеров"""
    name = models.CharField("Имя", max_length=150)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Фотка", upload_to="actors/%Y/%m/%d/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актёры и режиссёры"
        verbose_name_plural = "Актёры и режиссёры"


class Genre(models.Model):
    """Модель жанров"""
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    slug = models.SlugField("Слаг", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    """Модель для фильмов"""
    title = models.CharField("Название", max_length=150)
    tagline = models.CharField("Слоган", max_length=150, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/%Y/%m/%d/")
    date = models.DateField("Дата выхода")
    country = models.CharField("Страна выход", max_length=30)
    directors = models.ManyToManyField(People, verbose_name="Режиссёр", related_name="director_in_films")
    actors = models.ManyToManyField(People, verbose_name="Актёры", related_name="actor_in_films")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры", related_name="films")
    world_premiere = models.DateField("Премьера в мире")
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="Указать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="Указать сумму в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="Указать сумму в долларах")

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField("Слаг", max_length=150, unique=True)
    is_published = models.BooleanField("Статус публикации", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShot(models.Model):
    """Модель для кадров из фильма"""
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Кадр", upload_to="movie_shots/%Y/%m/%d/")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="shots", verbose_name="Фильм")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильмов"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
