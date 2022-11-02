from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context = {
        'Judul' : 'Blog Saya',
        'h1' : 'About Me',
        'Nama' : 'Valen Rionald',
        'NPM' : '1204060',
        'Asal' : 'Kuningan, Jawa Barat',
        'Email' : 'vrionald@gmail.com',
        'HP' : '089522910966',
        'Umur' : '20',
        'Desc' : 'Mahasiswa, Jomblo, Tersesat'
    }
    return render(request, 'blog/index.html', context)

def recent(request):
    return HttpResponse("RECENT BLOG")
    #context = {
    #    'Judul' : 'blog2',
    #    'h1' : 'Python'
    #}
    #return render(request, 'blog/index.html', context)
# Create your views here
