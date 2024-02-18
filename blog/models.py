from django.db import models
from django.urls import reverse


# Create your models here.
class Format(models.Model):
    img = models.ImageField(upload_to='img/index')
    name = models.CharField(max_length=150)
    bio = models.TextField()
    slug = models.SlugField(max_length=150)

    def get_absolute_url(self):
        return reverse("formatdetailview", args=[self.slug])

    def __str__(self):
        return self.name

class Consultation(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Register(models.Model):
    name = models.CharField(max_length=150)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='index/img')
    img1 = models.ImageField(upload_to='index/img')
    bio = models.TextField()
    tutor = models.CharField(max_length=150)
    price = models.IntegerField()
    count = models.IntegerField()
    numb = models.IntegerField()
    slug = models.SlugField(max_length=150)

    def get_absolute_url(self):
        return reverse("coursedetailview", args=[self.slug])

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=150)
    rank = models.CharField(max_length=150)
    age = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    phone = models.IntegerField()
    slug = models.SlugField(max_length=150)

    def get_absolute_url(self):
        return reverse("teamdetailview", args=[self.slug])
    def __str__(self):
        return self.name
