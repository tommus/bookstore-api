from django.contrib import admin

from bookstore.models import Author, Binding, Book, Publisher


# region Author Admin

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)
    list_per_page = 100
    search_fields = ("first_name", "last_name",)
    sortable_by = ("first_name", "last_name",)


admin.site.register(Author, AuthorAdmin)


# endregion

# region Binding Admin

class BindingAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_per_page = 100
    search_fields = ("description",)
    sortable_by = ("description",)


admin.site.register(Binding, BindingAdmin)


# endregion

# region Book Admin

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publisher", "binding", "release_date", "available",)
    list_per_page = 100
    search_fields = ("title", "author__first_name", "author__last_name", "publisher__name")
    sortable_by = ("title", "author", "publisher", "binding", "release_date", "available",)


admin.site.register(Book, BookAdmin)


# endregion

# region Publisher Admin

class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_per_page = 100
    search_fields = ("name",)
    sortable_by = ("name",)


admin.site.register(Publisher, PublisherAdmin)

# endregion
