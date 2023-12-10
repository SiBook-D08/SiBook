import json
from django.shortcuts import redirect, render
from favorite.models import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from favorite.forms import FavoritedBookForm

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    books = Book.objects.all()
    user = request.user
    context = {
        'username': request.user.username,
        'books': books,
        'user' : request.user,
    }
    return render(request, "favorite.html", context)

def get_books(request):
    product_item = Book.objects.filter(favorited=False)
    return HttpResponse(serializers.serialize('json', product_item))

def get_book_data(request, id):
    book = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', book))

def get_user_data(request, id):
    user = User.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', user))

@csrf_exempt
def add_to_favorited(request, id):
    if request.method == "POST":
        form = FavoritedBookForm(request.POST)
        if form.is_valid(): 
            book = Book.objects.get(pk=id)
            if not(FavoritedBooks.objects.filter(user=request.user, book=book).exists()):
                alasan = form.cleaned_data.get("alasan")
                favorited_book = FavoritedBooks(user=request.user, book=book, alasan=alasan)
                favorited_book.save()
                book.favorited = True
                book.save()

    return redirect('favorite:show_main')    

def get_favorited_books(request):
    favorited_books = FavoritedBooks.objects.all()
    return HttpResponse(serializers.serialize('json', favorited_books))

@csrf_exempt
def remove_from_favorited(request, id):
    if request.method == "POST":
        favorited_book = FavoritedBooks.objects.get(pk=id)
        book = favorited_book.book
        book.favorited = False
        book.save()
        favorited_book.delete()
        
    return redirect('favorite:show_main')

@csrf_exempt
def add_to_favorited_flutter(request, id):
    if request.method == "POST" :
        data = json.loads(request.body)
        book = Book.objects.get(pk=id)
        if not (FavoritedBooks.objects.filter(user=request.user, book=book).exists()):
            new_favorited_book = FavoritedBooks.objects.create(
                user = request.user,
                book = book,
                alasan = data["alasan"],
            )
            new_favorited_book.save()
            book.favorited = True
            book.save()
    return JsonResponse({"status": "success"}, status=200)