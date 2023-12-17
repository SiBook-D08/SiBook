from catalogue.models import Book
from donate.forms import BookForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def donate_view(request: HttpRequest):
    return render(request, 'donate.html', {})

@csrf_exempt
def add_book_ajax(request: HttpRequest):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse(status=302)
        
        obj = {'status': 'invalid'}
        form = BookForm(request.POST or None)
        if not form.is_valid():
            return HttpResponse(json.dumps(obj))
        
        obj['status'] = 'full'
        if Book.objects.all().count() >= 115:
            return HttpResponse(json.dumps(obj))
        
        obj['status'] = 'alrExists'
        book = None
        try:
            book = Book.objects.get(title=request.POST["title"])
        except:
            pass
        if book:
            return HttpResponse(json.dumps(obj))

        obj['status'] = 'valid'
        form.save()

        return HttpResponse(json.dumps(obj))
