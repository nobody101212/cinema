from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):  # ManyToMany (жанры)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    poster = models.ImageField(upload_to="posters/", blank=True, null=True)  # изображение

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="films"
    )

    genres = models.ManyToManyField(Genre, blank=True, related_name="films")  # ManyToMany

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year})"
