from django.shortcuts import render
from .models import Film

# Create your views here.

def products_list(request): 
    films = Film.objects.all().order_by("-created_at")
    return render(request, "movies/products.html", {"films": films})