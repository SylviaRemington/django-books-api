from django.db import models

# MODEL CREATION
class Book(models.Model):
# important - need def string (line 8) and return to actually see the data in the admin page.
# This is string data that helps with working with your admin area on localhost:8000/admin.
# Lines 8 and 9 calls string model and helps show on admin page what that is.
  def __str__(self):
    return f'{self.title} - a book by {self.author}'
  
  # models.CharField is the data type and means "string"
  title = models.CharField(max_length=80, unique=True)
  author = models.ForeignKey(
    # This line of authors.Author is the model and where it is coming from.
    "authors.Author", #This is the path to the Author model.
    related_name = "books", # This is the name of the reverse relation from Author to Book.
    on_delete = models.CASCADE # If the author is deleted, all their books are deleted.
  )
  genre = models.CharField(max_length=60)
  year = models.FloatField()

