from django.shortcuts import render, get_object_or_404
from .models import Film, Category


# Create your views here.

def products_list(request): 
    films = Film.objects.all().order_by("-created_at")
    return render(request, "movies/products.html", {"films": films})

def films_list(request):
    films = Film.objects.select_related("category").order_by("-created_at")
    return render(request, "movies/films/list.html", {"films": films})

def film_detail(request, pk):
    film = get_object_or_404(Film.objects.select_related("category"), pk=pk)
    return render(request, "movies/films/detail.html", {"film": film})

def categories_list(request):
    categories = Category.objects.order_by("name")
    return render(request, "movies/categories_list.html", {"categories": categories})