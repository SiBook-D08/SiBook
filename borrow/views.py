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
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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
def add_to_cart_flutter(request, book_id):
    # data = json.loads(request.body.decode('utf-8'))
    # uname = data.get('username', None)
    # print(request.body)
    username = request.POST.get('username', None)
    user_now = User.objects.get(username=username)
    if request.method == "POST" :
        book = Book.objects.get(pk=book_id)
        print("MASUKKK")
        if not (Cart.objects.filter(user=user_now, book=book).exists()):
            loan = Cart(user=user_now, book=book)
            loan.save()
            print("MASUK JUGA")
    return JsonResponse({"status": "success"}, status=200)

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
@csrf_exempt  
def add_to_list_flutter(request):
    username = request.POST.get('username', None)
    user_now = User.objects.get(username=username)
    if request.method == "POST" :
        cart = Cart.objects.filter(user = user_now, book__avaliable= True)
        for item in cart:
            loan = Loan(user=user_now, book=item.book)
            item.book.avaliable= False
            item.book.save()
            loan.save()
        Cart.objects.filter(user = user_now).delete()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
@csrf_exempt
def create_cart_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Cart.objects.create(
            user = request.user,
            book=["book"],
        )

        new_product.save()

    return JsonResponse({"status": "success"}, status=200)
    
    
@csrf_exempt
def create_list_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Cart.objects.create(
            user = request.user,
            book=["book"],
        )

        new_product.save()

    return JsonResponse({"status": "success"}, status=200)
    
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
    if request.method == "POST": 
        Cart.objects.filter(pk = id).delete()
    return redirect('borrow:show_main') 
@csrf_exempt 
def remove_from_cart_flutter (request, id):
    if request.method == "POST" :
        Cart.objects.get(book=Book.objects.get(pk=id)).delete()

    return JsonResponse({"status": "success"}, status=200)

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            author = form.cleaned_data.get("author")
            new_product = Request(title=title, author=author)
            new_product.save()
          
            return redirect('main:show_main')
    else:
        form = ProductForm()

        return HttpResponseRedirect(reverse('main:show_main'))




