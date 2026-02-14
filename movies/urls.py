from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .auth_views import register


urlpatterns = [
    path("", views.films_list, name="home"),
    path("products/", views.films_list, name="films_list"),
    path("products/create/", views.film_create, name="film_create"),
    path("products/<int:pk>/", views.film_detail, name="film_detail"),

    path("categories/", views.categories_list, name="categories_list"),
    path("categories/create/", views.category_create, name="category_create"),


    path("accounts/register/", register, name="register"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="movies/auth/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/logout/", views.logout_view, name="logout"),

]


