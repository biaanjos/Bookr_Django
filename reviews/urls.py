from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome_view'),
    path('<int:id>/', views.welcome_view_book, name='welcome_view_book'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_details, name='book_details'),
]
