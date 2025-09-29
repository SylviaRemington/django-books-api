from django.contrib import admin

# Register your models here.
#importing the book from class
from .models import Book

# Registering with the admin - so admin can see it
admin.site.register(Book)

# make migrations now