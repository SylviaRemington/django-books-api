from django.urls import path
from .views import CommentListView, CommentDetailView

# URLS.PY IS FOR THE PATHS - urls deal with the views
urlpatterns = [
  # If it's just endpoint of "/books" then it will be this view; however, if it has an id, it will be the next path below.
  path('', CommentListView.as_view()),

  # This below is Django's way of doing :id, and uses '<int:pk>' instead.
  # It expects it to have an integer which is called the pk.
  # Don't need to also add this path to the project urls.py because this falls under the books urls.
  path('<int:pk>/', CommentDetailView.as_view()),
]