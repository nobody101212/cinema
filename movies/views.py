from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Category
from .forms import FilmForm, CategoryForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def films_list(request):
    films = Film.objects.select_related("category").prefetch_related("genres").order_by("-created_at")

    cat = request.GET.get("category")
    if cat:
        films = films.filter(category__slug=cat)

    categories = Category.objects.order_by("name")
    return render(request, "movies/films/list.html", {"films": films, "categories": categories})


def film_detail(request, pk):
    film = get_object_or_404(Film.objects.select_related("category").prefetch_related("genres"), pk=pk)
    return render(request, "movies/films/detail.html", {"film": film})

@login_required
def film_create(request):

    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)  
        if form.is_valid():
            film = form.save()
            return redirect("film_detail", pk=film.pk)
    else:
        form = FilmForm()

    return render(request, "movies/films/create.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("films_list")


def categories_list(request):
    categories = Category.objects.order_by("name")
    return render(request, "movies/categories/list.html", {"categories": categories})


@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories_list")
    else:
        form = CategoryForm()

    return render(request, "movies/categories/create.html", {"form": form})
