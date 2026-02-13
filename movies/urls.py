from django.urls import path
from .views import products_list
from . import views

urlpatterns = [
    path("products/", products_list, name="products_list"),
]


urlpatterns = [
    path("", products_list),          
    path("products/", products_list),
]


urlpatterns = [
    path("", views.films_list, name="films_home"),           
    path("products/", views.films_list, name="films_list"),  
    path("products/<int:pk>/", views.film_detail, name="film_detail"),

    path("categories/", views.categories_list, name="categories_list"),
]
