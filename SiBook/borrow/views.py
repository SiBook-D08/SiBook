import json
from django.shortcuts import redirect, render
from django.urls import reverse
from borrow.forms import ProductForm
from borrow.models import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    books = Book.objects.all()
    user = request.user
    form = ProductForm(request.POST or None)
    context = {
        'name': request.user.username,
        'books': books,
        'user' : request.user,
        'form': form,
    }
    
    return render(request, "borrow.html", context)

@csrf_exempt
def add_to_cart(request, book_id):
    if request.method == "POST" :
        book = Book.objects.get(pk=book_id)
        if not (Cart.objects.filter(user=request.user, book=book).exists()):
            loan = Cart(user=request.user, book=book)
            loan.save()

    return redirect('borrow:show_main')
    
@csrf_exempt
def add_to_list(request):
    if request.method == "POST" :
        cart = Cart.objects.filter(user = request.user, book__avaliable= True)
        for item in cart:
            loan = Loan(user=request.user, book=item.book)
            item.book.avaliable= False
            item.book.save()
            loan.save()
        Cart.objects.filter(user = request.user).delete()
    return redirect('borrow:show_main')    

def batal_pinjem(request, id):
    print(Loan.objects.all())
    book = Book.objects.get(pk=id)
    print(request.user)
    return redirect('borrow:show_main')

def get_books(request):
    product_item = Book.objects.filter(avaliable=True)
    return HttpResponse(serializers.serialize('json', product_item))

def get_books_borrowed(request):
    product_item = Loan.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def get_book_data(request, id):
    book = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', book))

def get_user_data(request, id):
    user = User.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', user))

def get_cart(request):
    cart = Cart.objects.filter(user = request.user.id, book__avaliable= True)
    if len(cart)>0:
        return HttpResponse(serializers.serialize('json', cart), content_type="application/json")
    else:
        return HttpResponse(json.dumps(None), content_type="application/json")
    
@csrf_exempt    
def remove_from_cart (request, id):
    if request.method == "POST" :
        Cart.objects.filter(pk = id).delete()
    return redirect('borrow:show_main') 

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def add_request_ajax(request):
    if request.method == 'POST':
        title  = request.POST.get("title")
        author = request.POST.get("author")

        new_product = Request(title=title, author=author)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()



