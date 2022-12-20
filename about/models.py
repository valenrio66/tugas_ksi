from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    nama = models.CharField(max_length=25)
    alamat = models.TextField()
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.nama)
        super(Post, self).save()

    def __str__(self):
        return "{}".format(self.nama)