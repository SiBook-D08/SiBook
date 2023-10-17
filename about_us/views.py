from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def about_us_view(request: HttpRequest):
    return render(request, 'about_us.html')
