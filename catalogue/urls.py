from django.urls import path
from catalogue.views import *

app_name = 'catalogue'

urlpatterns = [
    path('', show_catalogue, name='show_catalogue'),
    path('add-new-data/', add_new_data, name='add_new_data'),
    path('get-books/', get_books, name='get_books'),
]