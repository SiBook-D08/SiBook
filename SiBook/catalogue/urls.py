from django.urls import path
from catalogue.views import *

app_name = 'catalogue'

urlpatterns = [
    path('', show_catalogue, name='show_catalogue'),
    path('add-new-data/', add_new_data, name='add_new_data'),
    path('get-books/', get_books, name='get_books'),
    path('edit-book/', edit_book, name='edit_book'),
    path('get-user-by-id/<int:id>/', get_user_by_id, name='get_user_by_id'),
    path('get-current-user/', get_current_user, name='get_current_user')
]