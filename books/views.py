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
  
  # Request is in json
  def post(self, request):
        # run it through the book serializer - running the data from parenthesis
        book_to_add = BookSerializer(data=request.data)
        try:
            # is valid is from our serializer
            # checked data through the model
            book_to_add.is_valid()
            # if valid then save
            book_to_add.save()
            # 201 is created and see that on Postman
            return Response(book_to_add.data, status=status.HTTP_201_CREATED)
        # exceptions are like a catch in js, but if we specify an exception like we do below then the exception thrown has to match to fall into it
        # For example the below is the exception thrown when we miss a required field
        # link: (this documentation entry is empty but shows it exists) https://docs.djangoproject.com/en/4.0/ref/exceptions/#django.db.IntegrityError
        except Exception as e:
            print('ERROR')
            # the below is necessary because two different formats of errors are possible. string or object format.
            # if it's string then e.__dict__ returns an empty dict {}
            # so we'll check it's a dict first, and if it's empty (falsey) then we'll use str() to convert to a string
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        

        
    



