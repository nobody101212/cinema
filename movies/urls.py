from django.urls import path
from . import views

urlpatterns = [
    path("", views.films_list),  # можно оставить как главная

    path("products/", views.films_list, name="films_list"),
    path("products/create/", views.film_create, name="film_create"),
    path("products/<int:pk>/", views.film_detail, name="film_detail"),
]
