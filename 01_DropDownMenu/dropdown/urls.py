from django.urls import path
from .views import dropdown, booksAPI, editbooksAPI

urlpatterns = [
    path('dropdown', dropdown),
    path('api/books', booksAPI.as_view(), name="books"),
    path('api/books/<int:pk>', editbooksAPI.as_view()),

]
