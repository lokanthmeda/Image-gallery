from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    category = models.CharField(max_length=20)
    date=models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={'pk':self.pk})


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.ImageField()

