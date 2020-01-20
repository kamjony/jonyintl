from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Service(models.Model):
    service_title = models.CharField(max_length=50)
    service_tagline = models.TextField(max_length=50)
    service_img = models.ImageField(upload_to='images/', blank=True)

class About(models.Model):
    about = RichTextField()

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_job = models.CharField(max_length=100)
    employee_image = models.ImageField(upload_to='images/')

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_logo = models.ImageField(upload_to='images/')

class GalleryImage(models.Model):
    gallery_name = models.CharField(max_length=50)
    gallery_image = models.ImageField(upload_to='images/')

class SpecialisedItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_detail = models.CharField(max_length=300)
    item_image = models.ImageField(upload_to='images/')
