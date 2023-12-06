from catalogue.models import Book
from donate.forms import BookForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
        form = form.save(commit=False)
        form.last_edited_user = request.user
        form.save()

        return HttpResponse(json.dumps(obj))


'''buat flutter'''
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_product = Book.objects.create(
            title = data["title"],
            author = (data["author"]),
            description = data["description"],
            num_pages = int(data["numPages"]),
            img_url = "https://books.google.com/books/content?id=SXGCEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            avaliable = True,
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)