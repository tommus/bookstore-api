from django.contrib import admin

from bookstore.models import Author, Binding, Book, Publisher


# region Author Admin

class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)


# endregion

# region Binding Admin

class BindingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Binding, BindingAdmin)


# endregion

# region Book Admin

class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)


# endregion

# region Publisher Admin

class PublisherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Publisher, PublisherAdmin)

# endregion
