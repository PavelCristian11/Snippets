from django.shortcuts import render
from .serializers import BookSerializer
from django.core import serializers
from rest_framework import generics, viewsets, filters
from .models import Books
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
def dropdown(request):
    #
    existing_books = Books.objects.all()
    #
    first_name = list(Books.objects.values_list('First name', flat=True).distinct())
    last_name = list(Books.objects.values_list('Last name', flat=True).distinct())
    publish_year = list(Books.objects.values_list('year', flat=True).distinct())
    #
    name = []
    #
    for i in range(len(first_name)):
        name.append(' '.join([first_name[i], last_name[i]]))
    #
    menu = {
        'Author': name,
        'Publish year': publish_year,
    }
    return render(request, 'home.html', {"all_books": existing_books, 'menu':menu})

# Books view

class booksAPI(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['First name', 'Last name', 'year']

class editbooksAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer