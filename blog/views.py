from multiprocessing import context
from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def index(request):
    db = Post.objects.all()
    context = {
        'Judul' : 'Blog Saya',
        'h1' : 'About Me',
        'Nama' : 'Valen Rionald',
        'NPM' : '1204060',
        'Asal' : 'Kuningan, Jawa Barat',
        'Email' : 'vrionald@gmail.com',
        'HP' : '089522910966',
        'Umur' : '20',
        'Desc' : 'Mahasiswa, Jomblo, Tersesat',
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post': db,
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

def update(request, id):
    obj = Post.objects.get(id=id)
    if request.method == 'POST':
        # Handle form submission
        form = PostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # Render the update form
        form = PostForm(instance=obj)
    return render(request, 'update.html', {'form': form})

# def create_blog(request):
#     if request.method == "POST":
#         form = Post(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('search/')
#             except:
#                 pass
#     else:
#         form = Post()
#     return render(request, 'create.html', {'form':form})