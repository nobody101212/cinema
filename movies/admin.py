from django.contrib import admin
from .models import Film, Category
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "genre", "created_at")
    search_fields = ("title", "genre")
    list_filter = ("year", "genre")

admin.site.register(Category)
admin.site.register(Film)