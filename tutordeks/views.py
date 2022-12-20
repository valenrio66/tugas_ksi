from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import context

def index(request):
    context = {
        'judul' : 'Home',
        'h2' : 'This is Home',
        'p' : 'Click the Button Below To See My Blog!'
    }
    return render(request, 'index.html', context)

def about(request):
    return render("Ini About")

def articles(request, year):
    year = year
    str = year
    return HttpResponse(year)