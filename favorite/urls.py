from django.urls import path
from favorite.views import *

app_name = 'favorite'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-books/', get_books, name='get_books'),
    path('get-book-data/<int:id>/', get_book_data, name="get_book_data"),
    path('get-user-data/<int:id>/', get_user_data, name="get_user_data"),
    path('add-to-favorited/<int:id>/', add_to_favorited, name="add_to_favorited"),
    path('get-favorited-books/', get_favorited_books, name="get_favorited_books" ),
    path('remove-from-favorited/<int:id>/', remove_from_favorited, name="remove_from_favorited"),
    path('add-to-favorited-flutter/<int:id>/', add_to_favorited_flutter, name="add_to_favorited_flutter"),
    path('remove-from-favorited-flutter/<int:id>/', remove_from_favorited, name="remove_from_favorited"),
    path('get-favorited-flutter/', get_favorited_flutter, name="get_favorited_flutter"),
]