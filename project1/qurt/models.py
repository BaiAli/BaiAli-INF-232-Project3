from tabnanny import verbose
from django.db import models
from django.urls import reverse


class Types(models.Model):
    nameoftypes = models.CharField(max_length=30)
    prices = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    photosofqurt = models.ImageField(upload_to ='images/', verbose_name="Фото", null=True)
def __str__(self):
        return self.title
def __str__(self):
        return self.photoofqurt + ": " + str(self.photoofqurt)

class Facts(models.Model):
    importantyears = models.CharField(max_length=30)  
    conclusion = models.CharField(max_length=250)
    famouspeople = models.CharField(max_length=50)
    def get_absolute_url(self):
        return reverse('id', args=[str(self.id)])

class Nationalparks(models.Model):
   name = models.CharField(max_length=30)
   location = models.CharField(max_length=250)
   datestarting = models.DateTimeField()


