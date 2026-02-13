from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Category
from .forms import FilmForm


# Create your views here.

def films_list(request):
    films = Film.objects.select_related("category").prefetch_related("genres").order_by("-created_at")

    # query params: /products/?category=marvel
    cat = request.GET.get("category")
    if cat:
        films = films.filter(category__slug=cat)

    categories = Category.objects.order_by("name")
    return render(request, "movies/films/list.html", {"films": films, "categories": categories})


def film_detail(request, pk):
    film = get_object_or_404(Film.objects.select_related("category").prefetch_related("genres"), pk=pk)
    return render(request, "movies/films/detail.html", {"film": film})


def film_create(request):
    # GET -> показать форму
    # POST -> сохранить данные
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)  # request.FILES нужен для картинки
        if form.is_valid():
            film = form.save()
            return redirect("film_detail", pk=film.pk)
    else:
        form = FilmForm()

    return render(request, "movies/films/create.html", {"form": form})
