from django.db import models

class author(models.Model):
    name = models.CharField(max_length=20)

class book(models.Model):
    title = models.CharField(max_length=30)
    authors = models.ManyToManyField(author)

class profile(models.Model):
    email = models.EmailField()
    phone_number = models.IntegerField()

class library(models.Model):
    number = models.PositiveIntegerField()

class personal(models.Model):
    profile = models.OneToOneField(profile , on_delete= models.CASCADE())
    library = models.ForeignKey(library , on_delete= models.CASCADE())
# Create your models here.
