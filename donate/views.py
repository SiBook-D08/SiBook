from catalogue.models import Book
from donate.forms import BookForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def donate_view(request: HttpRequest):
    return render(request, 'donate.html', {})

@csrf_exempt
def add_book_ajax(request: HttpRequest):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse(status=302)
        obj = {'status': 'full'}
        if Book.objects.all().count() >= 100:
            return HttpResponse(json.dumps(obj))
        obj['status'] = 'invalid'
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            obj['status'] = 'valid'

        return HttpResponse(json.dumps(obj))
