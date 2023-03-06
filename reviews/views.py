from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .utils import average_rating


def welcome_view(request):
    count = Book.objects.count()
    return render(request, 'base.html', {"book_counts": count})


def welcome_view_book(request, id):
    book = Book.objects.get(id=id)
    message = f"You have selected the {book.title} book!"
    return HttpResponse(message)


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews})
    context = {'book_list': book_list}
    # return render(request, 'reviews/books_list.html', context)
    return render(request, 'reviews/books_list_extended.html', context)


def book_details(request, id):
    from django.shortcuts import get_object_or_404

    book = get_object_or_404(Book, pk=id)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        number_of_reviews = len(reviews)
    else:
        book_rating = None
        number_of_reviews = 0

    book_data = [{'book': book, 'book_rating': book_rating}]
    context = {'book_data': book_data, 'reviews': reviews, 'number_of_reviews': number_of_reviews}
    return render(request, 'reviews/book_details.html', context)


