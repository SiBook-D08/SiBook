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
from .forms import EditBookForm


def show_catalogue(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'catalogue.html', context)

@csrf_exempt
def add_new_data(request):
    if Book.objects.all().count() >= 100: 
        return HttpResponse("Book slot is full", status=202)

    data = json.loads(request.body.decode('utf-8'))
    title = data.get('title', '')
    author = data.get('author', '')
    description = data.get('description', '')
    num_pages = data.get('num_pages', '') or 1
    img_url = data.get('img_url', '')
    avaliable = data.get('avaliable', '')
    
    new_book = Book(title=title, author=author, description=description, num_pages=num_pages, img_url=img_url, avaliable=avaliable)

    if len(Book.objects.filter(title=title)) == 0:
        new_book.save()
        return HttpResponse("Book Existed", status=201)

    return HttpResponse("Created", status=202)

def get_books(request):
    product_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def edit_book(request):
    data = json.loads(request.body.decode('utf-8'))
    edit_form = EditBookForm(data)
    if edit_form.is_valid():
        data = json.loads(request.body.decode('utf-8'))
        idBook = data.get('idBook', '')
        description = data.get('description', '')

        if Book.objects.filter(pk=idBook).count() == 0:
            return HttpResponse('Book does not exist', status=402)

        bookById = Book.objects.get(pk=idBook)
        bookById.description = description
        bookById.last_edited_user = request.user
        bookById.save()
        return JsonResponse({"status": "success"}, status=200)
    return JsonResponse({"status": "error"}, status=401)

def get_user_by_id(request, id):
    users = User.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', users))

def get_current_user(request):
    users = User.objects.filter(pk=request.user.pk)
    return HttpResponse(serializers.serialize('json', users))