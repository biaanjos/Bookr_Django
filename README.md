# Bookr_Django
Bookr Django project  - High-Level Programming Languages - Python - Final Project


Task 1: In this task, I want you to create a Python program named "load_data.py"
to read records from the "WebDevWithDjangoData.csv" file and update the
database. Then, you must call anything required from the load_data.py file in the
manage.py file to manipulate the database accordingly. In the end, use DB Browser
for SQLite to verify that all the tables are populated.

Task 2: In this task, you will implement a new view, template, and URL mapping,
to display these details of a book: title, publisher, publication date, and overall rating.
In addition to these details, the page should also show all the review comments,
specifying the name of the commenter and the dates on which the comments were
written and (if applicable) modified. The following steps will help you complete this
activity:

  1. Create a book details endpoint that extends the base template.
  2. Create a book details view that takes a specific book's primary key as the
  argument and returns an HTML page listing the book's details and any
  associated reviews.
  3. Do the required URL mapping in urls.py. The book details view URL should
  be http://0.0.0.0:8000/books/1/ (where 1 will represent the ID of the book
  accessed). You can use the get_object_or_404 method to retrieve the book
  with the given primary key.
  4. At the end of this task, you should be able to click the Reviews button on the
  book list page and get a detailed view of the book. The detail view should
  have all the details displayed in the following screenshot.
