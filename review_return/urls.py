from django.urls import path
from review_return.views import *

app_name = 'review_return'

urlpatterns = [

    path('', show_main, name='show_return'),
    path('get-books/', get_books, name='get_books'),
    path('get-books-borrowed/', get_books_borrowed, name='get_books_borrowed'),
    path('get-book-data/<int:id>/', get_book_data, name="get_book_data"),
    path('get-user-data/<int:id>/', get_user_data, name="get_user_data"),
    path('just-return-book/<int:id>/',just_return,name="just_return_book"),
    path('add-review/',review_and_return_books,name="review_and_return_book"),
    path('user-reviews/',show_review,name="show_reviews"),
    path('user-reviews/get-reviews/',get_reviews, name='get_reviews'),
    path('user-reviews/get-book-data/<int:id>/', get_book_data, name="get_book_data"),
    path('user-reviews/get-user-data/<int:id>/', get_user_data, name="get_user_data"),
    path('user-reviews/get-reviews-experimental/',get_reviews_experimental, name="get_reviews_experimental"),
    path('create-review-flutter/<int:id>/', create_review_flutter, name='create_product_flutter'),
    
]