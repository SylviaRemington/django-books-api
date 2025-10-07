from django.contrib import admin
# links through the project settings (get user model) to deliver the model
# So if we change what is in the project model, it will also change what is delivered here.
from django.contrib.auth import get_user_model #get the user model from project settings

# Register your models here
User = get_user_model()
admin.site.register(User) # then we'll register this to the admin as usual

