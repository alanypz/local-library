from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    num_genres=Genre.objects.all().count()
    num_book_titles_with_of=Book.objects.filter(title__icontains='of').count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_book_titles_with_of': num_book_titles_with_of},
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all().order_by('title')


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5

    def get_queryset(self):
        return Author.objects.all().order_by('last_name')


class AuthorDetailView(generic.DetailView):
    model = Author
