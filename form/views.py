from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import Post
from . import forms

# def index(request):
#     db = Post.objects.all()
#     context = {
#         'Judul' : 'Form Submit',
#         'SubJudul' : 'Forms | Valen Rionald',
#         'Nama' : 'Valen Rionald',
#         'NPM' : '1204060',
#         'Asal' : 'Kuningan, Jawa Barat',
#         'Email' : 'vrionald@gmail.com',
#         'HP' : '089522910966',
#         'Umur' : '20',
#         'Desc' : 'Mahasiswa, Jomblo, Tersesat',
#         'nama':'form',
#         'alamat':'form',
#         'tgl_lahir':'tgl_lahir',
#         'email':'email',
#         'post': db,
#     }

#     return render(request, 'form/index.html', context)

# def form(request):
#     classform = forms.classform()

#     context = {
#         'heading':'Form',
#         'classform': classform
#     }

#     if request.method == 'POST':
#         print("Ini adalah methode post")
#         Post.objects.create(
#             nama = request.POST['nama'],
#             alamat = request.POST['alamat'],
#             tgl_lahir = request.POST['tgl_lahir'],
#             email = request.POST['email'],
#         )
#         return HttpResponseRedirect('/form/')
    
#     else:
#         print("Ini adalah method GET")
#     return render(request, 'form/index.html', context)
#     #     context['nama'] = request.POST['nama']
#     #     context['alamat'] = request.POST['alamat']
#     #     context['tgl_lahir'] = request.POST['tgl_lahir']
#     #     context['email'] = request.POST['email']
#     #     context['namac'] = request.POST['namac']
#     #     context['alamatc'] = request.POST['alamatc']
#     #     context['tgl_lahirc'] = request.POST['tgl_lahirc']
#     #     context['emailc'] = request.POST['emailc']
#     #     return HttpResponseRedirect('/form/')
#     # else:
#     #     print("Ini adalah method GET")
#     # return render(request, 'form/index.html', context)

def index(request):
    # classform = forms.classform()

    # context = {
    #     'heading':'Home',
    #     'classform': classform
    # }

    # if request.method == 'POST':
    #     print("Ini adalah method POST")

    #     Post.objects.create(
    #         nama = request.POST['nama'],
    #         alamat = request.POST['alamat'],
    #         tgl_lahir = request.POST['tgl_lahir'],
    #         email = request.POST['email'],
    #     )
    #     return HttpResponseRedirect('form/index.html')

    # else:
    #     print("Ini adalah method GET")
    # return render(request, 'form/index.html', context)

    if request.method == 'POST':
        if request.POST.get('nama') and request.POST.get('alamat') and request.POST.get('tgl_lahir') and request.POST.get('email'):
            post = Post()
            post.nama = request.POST.get('nama')
            post.alamat = request.POST.get('alamat')
            post.tgl_lahir = request.POST.get('tgl_lahir')
            post.email = request.POST.get('email')
            post.save()

            return render(request, 'form/index.html')
    else:
        return render(request, 'form/index.html')

def recent(request):
    return HttpResponse("RECENT FORM")
    #context = {
    #    'Judul' : 'blog2',
    #    'h1' : 'Python'
    #}
    #return render(request, 'blog/index.html', context)
# Create your views here