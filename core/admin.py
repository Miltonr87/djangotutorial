from django.contrib import admin
from .models import Author, Book

# Register your models here.
admin.site.register(Author) # Register the Author model with the admin site
admin.site.register(Book) # Register the Book model with the admin site