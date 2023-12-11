from django.urls import path
from borrow.views import *

app_name = 'borrow'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-books/', get_books, name='get_books'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('add-to-cart-flutter/<int:book_id>/', add_to_cart_flutter, name='add_to_cart_flutter'),
    path('get-books-borrowed/', get_books_borrowed, name='get_books_borrowed'),
    path('get-book-data/<int:id>/', get_book_data, name="get_book_data"),
    path('get-user-data/<int:id>/', get_user_data, name="get_user_data"),
    path('get-cart/', get_cart, name="get_cart"),
    path('remove-cart/<int:id>/', remove_from_cart, name="remove_from_cart"),
    path('remove-cart-flutter/<int:id>/', remove_from_cart_flutter, name="remove_from_cart"),
    path('add-to-list/', add_to_list, name="add_to_list"),
    path('add-to-list-flutter/', add_to_list_flutter, name="add_to_list"),
    path('create_product/', create_product, name='create_product'),
    path('create-flutter/', create_cart_flutter, name='create_product_flutter'),
    path('create-flutter/', create_list_flutter, name='create_product_flutter'),
]