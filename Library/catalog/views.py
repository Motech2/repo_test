from django.shortcuts import render
from . import models


def index(request):
    """
    View function for home page
    """
    # generates count of the some of main object
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    # Available books
    avl_instances = models.BookInstance.objects.filter(status__exact='a').count()
    num_authors = models.Author.objects.count()  # the 'all()' is implied by default

    # Render the 'index.html' with the data in context
    return render(request,
                  'catalog/index.html',
                  context={'num_books': num_books, 'num_instances': num_instances, 'avl_instances': avl_instances,
                           'num_authors': num_authors})

