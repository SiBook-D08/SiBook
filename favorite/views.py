import json
from django.shortcuts import redirect, render
from favorite.models import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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
    product_item = Book.objects.filter(avaliable=True)
    return HttpResponse(serializers.serialize('json', product_item))

def get_book_data(request, id):
    book = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', book))

def get_user_data(request, id):
    user = User.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', user))

