from donate.forms import BookForm
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import redirect, render

# Create your views here.
def donate_view(request: HttpRequest):
    context = {}
    if (request.method == 'POST'):
        form = BookForm(request.POST or None)
        if (form.is_valid()):
            form.save()
            context['success'] = 1
        else:
            context['error'] = 1

    return render(request, 'donate.html', context)
