# so can import
#  Using rest framework - converts django from wanting to respond with its templating engine INTO wanting to send back JSON
from rest_framework.views import APIView # this imports rest_frameworks APIView that we'll use to extend to our custom view
from rest_framework.response import Response # Response gives us a way of sending a http response to the user making the request, passing back data and other information
from rest_framework import status # status gives us a list of official/possible response codes
# This is part of the rest framework - This is the import for the NotFound exception.
from rest_framework.exceptions import NotFound

# import the IsAuthenticaticatedOnReadOnly - can do things on GET requests
from rest_framework.permissions import IsAuthenticatedOrReadOnly # IsAuthenticatedOrReadOnly specifies that a view is secure on all methods except get requests

# ! I might need to comment out line 13 as per Tristan's code
from .models import Comment
from .serializers import CommentSerializer #ADD THIS


# Create your views here.
# Need to fully create class CommentListView so that everything works out correctly.
class CommentListView(APIView):
    def post(self, request):
        print("CREATING COMMENT WITH USER ID", request.user.id)
        #ADD THIS BELOW
        request.data['owner'] = request.user.id 
        comment_to_add = CommentSerializer(data=request.data)
        try:
            comment_to_add.is_valid()
            comment_to_add.save()
            return Response(comment_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("ERROR")
            # error msg - if the error message comes with an explainer message, then send that.
            # if there's a nice readable error, then send that back; otherwise...
            # otherwise, stringify the error
            return Response(e.__dict__ if e.__dict__ else (str(e)), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class CommentDetailView(APIView):
    def get(self, request):
        print("Get A Comment")



# THIS CURRENT PART BELOW IS WHAT TRISTAN HAS FROM LINES 17 TO 38 ABOVE (IN PLACE OF THAT):
# class CommentListView(APIView):
#     permission_classes = (IsAuthenticated, )

#     def post(self, request):
#         print("CREATING COMMENT WITH USER ID", request.user.id)
#         request.data['owner'] = request.user.id
#         comment_to_add = CommentSerializer(data=request.data)
#         try:
#             comment_to_add.is_valid()
#             comment_to_add.save()
#             return Response(comment_to_add.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             print("ERROR")
#             return Response(e.__dict__ if e.__dict__ else (str(e)), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


# class CommentDetailView(APIView):
#     def get(self, request):
#         print("GET A COMMENT")

