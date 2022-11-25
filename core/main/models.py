from django.db import models

# Create your models here.
class sunglasses(models.Model):
    img = models.ImageField(upload_to='media')

class aboutus(models.Model):
    img = models.ImageField(upload_to='media')
    tag = models.CharField('Tag', max_length=30)
    txt = models.TextField('Text')

class ourglasses(models.Model):
    img = models.ImageField(upload_to='media')
    tag = models.CharField('Tag', max_length=30)
    prs = models.IntegerField('Price')