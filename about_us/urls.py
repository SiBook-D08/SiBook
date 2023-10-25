from django.urls import path
from about_us.views import *

app_name = 'about_us'

urlpatterns = [
    path('', about_us_view, name='about_us_view'),
]