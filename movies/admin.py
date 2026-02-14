from django.contrib import admin
from .models import Film, Category, Genre

admin.site.register(Category)
admin.site.register(Genre)



@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "category")
    list_filter = ("category", "genres", "year")
    search_fields = ("title",)
    filter_horizontal = ("genres",)


