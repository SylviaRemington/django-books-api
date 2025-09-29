from django.db import models

# Create your models here.
class Book(models.Model):
#   important
  def __str__(self):
    return f'{self.title} - {self.author}'
  title = models.CharField(max_length=80, unique=True)
  author = models.CharField(max_length=50)
  genre = models.CharField(max_length=60)
  year = models.FloatField()