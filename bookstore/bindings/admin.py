from django.contrib import admin
from django.contrib.admin import register

from bookstore.bindings.models import Binding


@register(Binding)
class BindingAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_per_page = 100
    search_fields = ("description",)
    sortable_by = ("description",)
