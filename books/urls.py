from django.urls import path
from .views import BookListView, BookDetailView

# URLS.PY IS FOR THE PATHS - urls deal with the views
urlpatterns = [
  path('', BookListView.as_view()),
  path('<int:pk/', BookDetailView.as_view()),
]
