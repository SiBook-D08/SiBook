from django.contrib import admin
from favorite.models import *

# Register your models here.
admin.site.register(Favorite)
admin.site.register(FavoritedBooks)