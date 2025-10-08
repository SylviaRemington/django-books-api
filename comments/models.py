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
        on_delete=models.CASCADE #If the book is deleted, all the comments are deleted. But you can delete a comment separately.
    ),

    # When someone creates a comment, here we are relating data to it.
    # We can't do user on a model because it clashes with Django and special words.
    owner = models.ForeignKey(
        "jwt_auth.User",
        related_name="comments",
        on_delete=models.CASCADE,
        editable=False,
    )
    