from django.shortcuts import render, get_object_or_404
from .models import Book, Author

def book_list(request):
    books = Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'core/book_detail.html', {'book': book})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'core/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'core/author_detail.html', {'author': author})