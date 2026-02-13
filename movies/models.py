from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="films"
    )

    def __str__(self):
        return f"{self.title} ({self.year})"

    def get_absolute_url(self):
        return
