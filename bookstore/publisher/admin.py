from django.contrib import admin
from django.contrib.admin import register

from bookstore.publisher.models import Publisher


@register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_per_page = 100
    search_fields = ("name",)
    sortable_by = ("name",)
