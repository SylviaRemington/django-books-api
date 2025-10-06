from rest_framework import serializers
from .models import Book
from authors.serializers import AuthorSerializer
from comments.serializers import CommentSerializer

# Serializer takes the data and swaps it from Postgres to JSON, and JSON to Postgres, and handles that transaction.
# Handles that transaction between the different data forms
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    # converts all fields from json to sql
    fields = '__all__'

# This builds on the book serializer.
class PopulatedBookSerializer(BookSerializer):
    author = AuthorSerializer()
    comments = CommentSerializer(many=True)
