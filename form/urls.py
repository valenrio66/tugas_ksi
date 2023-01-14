from django.urls import path
from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index, name='index'),
    path('daftar/', views.daftar, name='daftar'),
    path('recent/', views.recent, name='recent'),
    path('post/', views.recent, name='post'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]