# so can import
#  Using rest framework - converts django from wanting to respond with its templating engine INTO wanting to send back JSON
from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
# This is part of the rest framework - This is the import for the NotFound exception.
from rest_framework.exceptions import NotFound


from .models import Book
from .serializers import BookSerializer

# VIEWS.PY SECTION IS FOR THE FUNCTIONS
# Create your views here.
# Extends our base class of API view
class BookListView(APIView):
  
  # GET REQUEST -- Ability to have a read all and getting all of the data.
  # All of our requests need to take self, and talking about this view, this request view / the request object(?).
  # The request is in JSON.
  def get(self, _request):
    # Can use def get or def post or def put or def delete
    # Defining all the methods that this view can respond to.
    # This gets all the books. Gets everything from the db through the model.
    books = Book.objects.all()
    # passes through the serializer - "I'm expecting a list of books.""
    # Serializing it - so doing the transition from Postgres to JSON or vice versa.
    # When we want to pass a lot of them, we use the many=True argument.
    serialized_books = BookSerializer(books, many=True)
    # return a response - with the serialized response data & the appropriate HTTP code.
    # This gives us the ability to now test it in Postman.
    return Response(serialized_books.data, status=status.HTTP_200_OK)
  
#------------------------------------------------------------------

  # POST REQUEST -- Ability to create data here.
  # Request is in json. That's what the request body is being sent as.
  # Defining what happens when a post method is sent to that request, sent to that endpoint.
  def post(self, request):
        # We run this so that it is something that can be stored in our database.
        # So we run it through the book serializer - running the data from parenthesis.
        # The data is the request.data.
        # It's passing the request body, but through the serializer.
        # The serializer returns the book to add. But there are a few diff features on it that checks if the data is valid against the model.
        book_to_add = BookSerializer(data=request.data)
        try:
            # "is valid" is coming from the serializer. And the serializer is coming from rest framework. So checking it's valid against the model.
            # Checking data through the model to see if it's valid.
            book_to_add.is_valid()
            # If it is valid, then saves it.
            book_to_add.save()
            # 201 is created and see that on Postman.
            # Then we return the data, and then HTTP 201 is created which you see in POSTMAN in the output Body part at bottom.
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
        

#------------------------------------------------------------------

# CREATING SHOWPAGE
# Creating the book detail view.
class BookDetailView(APIView):
    # pk stands for primary key, which is the ID.
    def get(self, _request, pk):
        try:
            # book is the model and we pass in the primary key as the argument.
            book = Book.objects.get(pk=pk)
            # Now we want a serialized book, same as before when using the get request. (get book, serialize them, and then return them.)
            serialized_book = BookSerializer(book)
            # Return the response.
            return Response(serialized_book.data, status=status.HTTP_200_OK)
        # Looking at exceptions - in case there's a book that doesn't exist. Like a catch.
        except Book.DoesNotExist:
            # NotFound is a specific error, a 404 error.
            # Need to import it and it comes from the exceptions in the the Djano rest framework.
            raise NotFound(detail="🆘 Can't find that book!")
        
        # Now we want this function to respond to a particular url.
        
#------------------------------------------------------------------
    

