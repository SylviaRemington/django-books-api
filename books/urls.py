from django.urls import path
from .views import BookListView, BookDetailView

# URLS.PY IS FOR THE PATHS - urls deal with the views
urlpatterns = [
  path('', BookListView.as_view()),

  # This below is Django's way of doing :id, and uses '<int:pk/' instead.
  # It expects it to have an integer which is called the pk.
  path('<int:pk/', BookDetailView.as_view()),
]

