from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound # This provides a default response for a not found

from .models import Author
from .serializers import AuthorSerializer

# Create your views here.

class AuthorListView(APIView):

    # handle a GET request in the BookListView
    def get(self, _request):
        # go to the database and get all the authors
        authors = Author.objects.all()
        # translate the books from the database to a usable form
        serialized_authors = AuthorSerializer(authors, many=True)
        # return the serialized data and a 200 status code
        return Response(serialized_authors.data, status=status.HTTP_200_OK)

    def post(self, request):
        author_to_add = AuthorSerializer(data=request.data)
        try:
           author_to_add.is_valid()
           author_to_add.save()
           return Response(author_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error")
            # the below is necessary because two different formats of errors are possible. string or object format.
            # if it's string then e.__dict__ returns an empty dict {}
            # so we'll check it's a dict first, and if it's empty (falsey) then we'll use str() to convert to a string
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        