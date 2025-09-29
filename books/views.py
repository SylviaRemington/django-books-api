# so can import
from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes

from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BookListView(APIView):

  def get(self, _request):
    # Can use def get or def post or def put or def delete
    # gets all the books
    books = Book.objects.all()
    # passes through the serializer - I'm expecting a list of books
    serialized_books = BookSerializer(books, many=True)
    # return a response
    return Response(serialized_books.data, status=status.HTTP_200_OK)
