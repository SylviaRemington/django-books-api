from django.db import models

# Create your models here.
class Comment(models.Model):
    def __str__(self):
        return f'{self.text} - {self.book}'
    text = models.TextField(max_length=300)
    # auto now true means that when a comment is created it will add a timestamp
    # This will automatically set the created_at field to the current date and time when the comment is created.
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(
        "books.Book",
        related_name = "comments",
        on_delete=models.CASCADE
    )