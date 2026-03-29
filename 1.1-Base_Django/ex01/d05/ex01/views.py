from django.shortcuts import render


# Create your views here.
def django_page(request):
    return render(request, 'ex01/django.html')


def display_page(request):
    return render(request, 'ex01/display.html')


def templates_page(request):
    return render(request, 'ex01/templates.html')
