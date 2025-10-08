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
    # User is a Django reserved thing so can't use it.

    # The owner of a comment will be models.ForeignKey
    # Like the author of a book is the ForeignKey of "authors.Author"
    owner = models.ForeignKey(
        # ! DON'T UNDERSTAND LINE 25 BELOW AND WHY we are using jwt_auth.User when books is authors.Author
        # The reverse relation here.
        # A comment will have an owner. But an owner will have many comments.
        "jwt_auth.User",
        # So the related name will have comments - because owner will have comments.
        related_name="comments",
        on_delete=models.CASCADE
    )
