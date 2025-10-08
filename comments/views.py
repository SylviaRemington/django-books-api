# so can import
#  Using rest framework - converts django from wanting to respond with its templating engine INTO wanting to send back JSON
from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
# This is part of the rest framework - This is the import for the NotFound exception.
from rest_framework.exceptions import NotFound

# import the IsAuthenticaticatedOnReadOnly - can do things on GET requests
from rest_framework.permissions import IsAuthenticatedOrReadOnly # IsAuthenticatedOrReadOnly specifies that a view is secure on all methods except get requests


from .models import Comment
from .serializers import CommentSerializer


# Create your views here.
# Need to fully create class CommentListView so that everything works out correctly.
class CommentListView(APIView):
    def post(self, request):
        print("CREATING COMMENT WITH USER ID", request.user.id)
        # request.data['owner'] = request.user.def form_invalid(self, form):
        #     response = super().form_invalid(form)
        #     comment_to_add
        
class CommentDetailView(APIView):
    def get(self, request):
        print("Get A Comment")
