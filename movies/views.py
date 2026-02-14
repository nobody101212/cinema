from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Category, Genre
from .forms import FilmForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q



# Create your views here.



def films_list(request):
    films = Film.objects.select_related("category").prefetch_related("genres").all()

    q = request.GET.get("q", "").strip()
    if q:
        films = films.filter(Q(title__icontains=q) | Q(description__icontains=q))

    selected_category = request.GET.get("category", "").strip()
    if selected_category:
        films = films.filter(category__slug=selected_category)

    selected_year = request.GET.get("year", "").strip()
    if selected_year == "2000":
        films = films.filter(year__gte=2000, year__lt=2010)
    elif selected_year == "2010":
        films = films.filter(year__gte=2010, year__lt=2020)
    elif selected_year == "2020":
        films = films.filter(year__gte=2020)

    selected_genres = request.GET.getlist("genres")  # список строк
    if selected_genres:
        films = films.filter(genres__id__in=selected_genres).distinct()

    films = films.order_by("-id")

    categories = Category.objects.order_by("name")
    genres = Genre.objects.order_by("name")

    return render(request, "movies/films/list.html", {
        "films": films,
        "categories": categories,
        "genres": genres,
        "q": q,
        "selected_category": selected_category,
        "selected_year": selected_year,
        "selected_genres": selected_genres,
    })

    
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

def film_create(request):
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("films_list")
    else:
        form = FilmForm()

    return render(request, "movies/films/create.html", {"form": form})