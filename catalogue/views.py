import datetime
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import render, redirect
from django.urls import reverse
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book

def show_catalogue(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'catalogue.html', context)

@csrf_exempt
def add_new_data(request):
    data = json.loads(request.body.decode('utf-8'))
    title = data.get('title', '')
    publisher = data.get('publisher', '')
    description = data.get('description', '')
    num_pages = data.get('num_pages', '') or 1
    avaliable = data.get('avaliable', '')
    
    new_book = Book(title=title, publisher=publisher, description=description, num_pages=num_pages, avaliable=avaliable)

    if len(Book.objects.filter(title=title)) == 0:
        new_book.save()
        return HttpResponse("CREATED", status=201)

    return HttpResponse("Book Existed", status=202)

def get_books(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))