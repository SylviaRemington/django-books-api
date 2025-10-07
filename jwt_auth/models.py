# This line 2 already has pwd confirmation, pwd, username as keys on that model from Django out of the box
from django.db import models
from django.contrib.auth.models import AbstractUser # user model that already exists in django

# Models here:
# This is inheriting, because we are extending the AbstractUser.
class User(AbstractUser): # we extend the AbstractUser and add the fields that we want for our users
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=350)