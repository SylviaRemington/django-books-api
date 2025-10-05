from django.contrib import admin

# Register your models here - You're registering the app in the admin.py
# Need to register it so it shows up when we log into the browser.
#importing the book from class
from .models import Book

# Registering with the admin - so admin can see it
admin.site.register(Book)

# make migrations now