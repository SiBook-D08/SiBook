from django.urls import path
from borrow.views import *

app_name = 'borrow'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-books/', get_books, name='get_books'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('get-books-borrowed/', get_books_borrowed, name='get_books_borrowed'),
    path('get-book-data/<int:id>/', get_book_data, name="get_book_data"),
    path('get-user-data/<int:id>/', get_user_data, name="get_user_data"),
]