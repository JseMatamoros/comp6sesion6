from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book

class IndexPageView(TemplateView):
    template_name = 'index.html'

def list_books(request):
    books = Book.objects.all()
    books_value = Book.objects.filter(valoracion__gt=1500)
    context = {
        'books': books,
        'books_value': books_value
    }
    return render(request, 'list_books.html', context)