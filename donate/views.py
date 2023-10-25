from donate.forms import BookForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def donate_view(request: HttpRequest):
    context = {}
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect("/login/")
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            context['success'] = 1
        else:
            context['error'] = 1

    return render(request, 'donate.html', context)

@csrf_exempt
def add_book_ajax(request: HttpRequest):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse(status=302)
        obj = {'isValid': False}
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            obj['isValid'] = True

        return HttpResponse(json.dumps(obj))
