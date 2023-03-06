def create_publisher(p_name, p_website, p_email):
    from reviews.models import Publisher
    publisher = Publisher(name=p_name, website=p_website, email=p_email)
    publisher.save()


def create_book(b_title, b_pubdate, b_isbn, b_pub_name):
    from reviews.models import Book, Publisher
    from datetime import datetime
    publisher = Publisher.objects.get(name=b_pub_name)

    formatter = '%Y/%m/%d'
    p_date = datetime.strptime(b_pubdate, formatter)

    Book.objects.create(title=b_title, publication_date=datetime(p_date.year, p_date.month, p_date.day),
                        isbn=b_isbn, publisher=publisher)


def create_contributor(f_name, l_name, c_email):
    from reviews.models import Contributor
    Contributor.objects.create(first_names=f_name, last_names=l_name, email=c_email)


def create_book_contributor(c_book, c_name, role):
    from reviews.models import Book, Contributor, BookContributor

    contributor = Contributor.objects.get(email=c_name)
    book = Book.objects.get(title=c_book)

    book_contributor = BookContributor(book=book, contributor=contributor, role=role)
    book_contributor.save()


def create_review(r_content, r_rating, r_date_created, r_date_edited, r_creator, r_book):
    from reviews.models import Book, Review
    from datetime import datetime
    from django.contrib.auth.models import User

    book = Book.objects.get(title=r_book)
    creator_id = User.objects.get(email=r_creator)

    formatter = '%Y-%m-%d %H:%M:%S.%f'
    datetime_review = datetime.strptime(r_date_created, formatter)
    datetime_edited = datetime.strptime(r_date_edited, formatter)

    review = Review(content=r_content, rating=int(r_rating),
                    date_created=datetime(datetime_review.year, datetime_review.month, datetime_review.day,
                                          datetime_review.hour, datetime_review.minute, datetime_review.second,
                                          datetime_review.microsecond),
                    date_edited=datetime(datetime_edited.year, datetime_edited.month, datetime_edited.day,
                                         datetime_edited.hour, datetime_edited.minute, datetime_edited.second,
                                         datetime_edited.microsecond),
                    creator=creator_id, book=book)
    review.save()


def delete():
    from reviews.models import Contributor, Publisher, Book, BookContributor, Review
    Publisher.objects.all().delete()
    """Contributor.objects.all().delete()
    Book.objects.all().delete()
    BookContributor.objects.all().delete()
    Review.objects.all().delete()"""


def load():
    csv_file = open('WebDevWithDjangoData.csv', 'r')
    line = 0
    table_name = ''

    for row in csv_file:
        row = row.replace('\n', '').split(',')
        if row[0].startswith('content'):
            print("New table")
            table = row[0]
            table_name = table.split(':')[1]
            print('table name is', table_name)
            line = 0
        else:
            line += 1
            if line == 1:
                print('Column are', row[0], row[1], row[2])
            else:
                if table_name == 'Publisher' and row[0] != '':
                    create_publisher(row[0], row[1], row[2])
                elif table_name == 'Book' and row[0] != '':
                    create_book(row[0], row[1], row[2], row[3])
                elif table_name == 'Contributor' and row[0] != '':
                    create_contributor(row[0], row[1], row[2])
                elif table_name == 'BookContributor' and row[0] != '':
                    create_book_contributor(row[0], row[1], row[2])
                elif table_name == 'Review' and row[0] != '':
                    create_review(row[0], row[1], row[2], row[3], row[4], row[5])
                print("Content is", row[0], row[1], row[2])

    csv_file.close()


"""if table_name == 'Publisher' and row[0] != '':
     create_publisher(row[0], row[1], row[2])
elif table_name == 'Book' and row[0] != '':
        create_book(row[0], row[1], row[2], row[3])
elif table_name == 'Contributor' and row[0] != '':
        create_contributor(row[0], row[1], row[2])
                        elif table_name == 'Contributor' and row[0] != '':
                    create_contributor(row[0], row[1], row[2])
                                  elif table_name == 'BookContributor' and row[0] != '':
                    create_book_contributor(row[0], row[1], row[2])"""