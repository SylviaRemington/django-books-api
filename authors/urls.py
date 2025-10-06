from django.urls import path
from .views import AuthorListView

urlpatters = [
    path('', AuthorListView.as_view()),
]