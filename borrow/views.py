from django.shortcuts import redirect, render
from borrow.models import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def show_main(request):
    books = Book.objects.all()
    user = request.user
    
    context = {
        'name': request.user.username,
        'books': books,
        'user' : request.user,
    }
    
    return render(request, "borrow.html", context)

@csrf_exempt
def add_to_cart(request, book_id):
    book = Book.objects.get(pk=book_id)
    loan = Loan(user=request.user, book=book)
    loan.save()
    book.avaliable = False
    book.save()
    print(len(Loan.objects.all()))
    return redirect('borrow:show_main')
    
    

def batal_pinjem(request, id):
    print(Loan.objects.all())
    book = Book.objects.get(pk=id)
    Loan.objects.filter(user=request.user, book=book).delete()
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