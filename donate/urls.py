from django.urls import path
from donate.views import *

app_name = 'donate'

urlpatterns = [
    path('', donate_view, name='donate_view'),
    path('add-book-ajax/', add_book_ajax, name='add_book_ajax'),
]
