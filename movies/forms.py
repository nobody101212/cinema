from django import forms
from .models import Film, Category

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ["title", "year", "description", "category", "genres", "poster"]

    def clean_title(self):
        title = (self.cleaned_data.get("title") or "").strip()
        if len(title) < 2:
            raise forms.ValidationError("Название слишком короткое.")
        return title

    def clean_year(self):
        year = self.cleaned_data.get("year")
        if year < 1888 or year > 2100:
            raise forms.ValidationError("Год должен быть в диапазоне 1888–2100.")
        return year

    def clean_poster(self):
        poster = self.cleaned_data.get("poster")
        if poster:

            if poster.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Файл слишком большой (макс 5MB).")
        return poster

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug"]

    def clean_name(self):
        name = (self.cleaned_data.get("name") or "").strip()
        if len(name) < 2:
            raise forms.ValidationError("Название категории слишком короткое.")
        return name

    def clean_slug(self):
        slug = (self.cleaned_data.get("slug") or "").strip().lower()

        import re
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            raise forms.ValidationError("Slug только латиница, цифры и дефисы. Пример: action, sci-fi")
        return slug

