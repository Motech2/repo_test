from django.db import models
from django.urls import reverse
import uuid


class Author(models.Model):
    """
    Model representing an Author.
    """
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    Birth = models.DateField('Birth', null=True, blank=True)
    Death = models.DateField('Death', null=True, blank=True)

    def get_absolute_url(self):
        """
        returns The url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.Fname, self.Lname)


class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 character <a href="https://isbn-international.org">ISBN</a>')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        returns The url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e , that can be borrowed from the library)
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    Loan_status = (
        ('m', 'Maintenance'),
        ('o', 'on loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )
    status = models.CharField(max_length=1, choices=Loan_status, blank=True, default='m', help_text='Book Availability')


class Meta:
    ordering = ['due_back']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, (%s)' % (self.id, self.book.title)


class Genre(models.Model):
    """
    Model representing a book genre
    """
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc)')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name
