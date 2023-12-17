import json
from django.shortcuts import redirect, render
from borrow.models import *
from review_return.models import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def show_review(request):
    reviewedBooks = GiveBack.objects.all()
    
    context = {
        'name': request.user.username,
        'reviewed_books': reviewedBooks,
    }
    return render(request, "book_review.html",context)

@login_required(login_url='/login')

# Create your views here.
def show_main(request):
    borrowedBooks = Loan.objects.all()
    user = request.user
    
    context = {
        'name': request.user.username,
        'books': borrowedBooks,
        'user' : request.user,
    }
    return render(request, "review_return.html",context)


#Make it so you delete from Loan Model and add a review IF text field isnt empty
@csrf_exempt
def just_return(request, id):
    if request.method=='POST':
        book = Book.objects.get(pk=id)
        Loan.objects.filter(user=request.user, book=book).delete()
        book.avaliable = True
        book.save()
        return JsonResponse({'message': 'Book returned successfully.'}, status=200)

@csrf_exempt
def review_and_return_books(request):
    bad_desc_list = ['bagus', 'keren banget', 'serem bukunyaa']
    for desc in bad_desc_list:
        if len(GiveBack.objects.filter(review__contains=desc)) == 0 :
            continue
        bad_review = GiveBack.objects.get(review__contains=desc)
        bad_review.delete()
    if request.method == 'POST':
        user_id = request.POST.get("user")
        book_id = request.POST.get("book")
        review = request.POST.get("review")
        user = User.objects.get(pk=user_id)
        book = Book.objects.get(pk=book_id)

        new_review = GiveBack(user=user, book=book, review=review)
        new_review.save()
        just_return(request,book_id)

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

#have to change this to get borrowed books
def get_books(request):
    product_item = Book.objects.filter(avaliable=True)
    return HttpResponse(serializers.serialize('json', product_item))

def get_books_borrowed(request):
    product_item = Loan.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

def get_book_data(request, id):
    book = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', book))

def get_user_data(request, id):
    user = User.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', user))

def get_reviews(request):
    review=GiveBack.objects.all()
    return HttpResponse(serializers.serialize('json', review))

def get_reviews_experimental(request):
    reviews = GiveBack.objects.select_related('book').all()
    return HttpResponse(serializers.serialize('json', reviews))

@csrf_exempt
def create_review_flutter(request,id):
    if request.method == 'POST':
        book=Book.objects.get(pk=id)
        data = json.loads(request.body)

        new_product = GiveBack.objects.create(
            user = request.user,
            book = book,
            review = data["review"]
        )

        new_product.save()
        just_return(request,id)

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)