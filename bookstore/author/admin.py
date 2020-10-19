from django.contrib import admin
from django.contrib.admin import register

from bookstore.author.models import Author


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)
    list_per_page = 100
    search_fields = ("first_name", "last_name",)
    sortable_by = ("first_name", "last_name",)
