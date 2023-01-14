from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import Post

def index(request):
    db = Post.objects.all()
    context = {
        'post': db,
    }
    if request.method == 'POST':
        if request.POST.get('nama') and request.POST.get('alamat') and request.POST.get('tgl_lahir') and request.POST.get('email'):
            post = Post()
            post.nama = request.POST.get('nama')
            post.alamat = request.POST.get('alamat')
            post.tgl_lahir = request.POST.get('tgl_lahir')
            post.email = request.POST.get('email')
            post.save()

            return render(request, 'form/daftar.html', context)
    else:
        return render(request, 'form/index.html')

def recent(request):
    return HttpResponse("RECENT FORM")

def daftar(request):
    db = Post.objects.all()
    context = {
        'post': db,
    }
    return render(request, 'form/daftar.html', context)

def update(request):
    db = Post.objects.all()
    context = {
        'post': db,
    }
    return render(request, 'form/daftar.html', context)

def delete(request, id):
    db = Post.objects.all()
    context = {
        'post': db,
    }
    Post.objects.filter(id=id).delete()
    return render(request, 'form/daftar.html', context)