from django.contrib import admin
from django.contrib.auth import get_user_model #get the user model from project settings

# Register your models here
User = get_user_model()
admin.site.register(User) # then we'll register this to the admin as usual

