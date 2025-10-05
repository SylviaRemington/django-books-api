from django.db import models

# MODEL CREATION
class Book(models.Model):
# important - need def string and return to actually see the data
# This is string data that helps with working with your admin area on localhost:8000/admin
  def __str__(self):
    return f'{self.title} - a book by {self.author}'
  title = models.CharField(max_length=80, unique=True)
  author = models.CharField(max_length=50)
  genre = models.CharField(max_length=60)
  year = models.FloatField()
