from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'SiBook'
    }
    return render(request, 'main.html', context)