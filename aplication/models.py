from django.db import models

# Create your models here.

class Forums(models.Model):
    image = models.ImageField(upload_to='main_images')
    title = models.CharField(max_length=255)
    min_desc = models.CharField(max_length=255)
    description = models.TextField()
    tg_username = models.CharField(max_length=255, null=True, blank=True)

class News(models.Model):
    image = models.ImageField(upload_to='main_images')
    title = models.CharField(max_length=255)
    min_desc = models.CharField(max_length=255)
    description = models.TextField()
    tg_username = models.CharField(max_length=255, null=True, blank=True)