
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
    bio = models.TextField()
    month = models.IntegerField()
    slug = models.SlugField(max_length=150)

    def get_absolute_url(self):
        return reverse("coursedetailview", args=[self.slug])

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=150)
    rank = models.CharField(max_length=150)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=150)

    def get_absolute_url(self):
        return reverse("teamdetailview", args=[self.slug])
    def __str__(self):
        return self.name


class Time_lesson(models.Model):
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.time

class Date(models.Model):
    date = models.CharField(max_length=100)
    time = models.ManyToManyField(Time_lesson)
    def __str__(self):
        return self.date

class Lesson(models.Model):
    name = models.CharField(max_length=150)
    lesson_date = models.ManyToManyField(Date)
    def __str__(self):
        return self.name


class Header(models.Model):
    title = models.CharField(max_length=200)
    bio = models.TextField()
    numb = models.CharField(max_length=20)

    def __str__(self):
        return self.numb

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='index/img')
    comment = models.TextField()
    job = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    def get_absolute_url(self):
        return reverse("testimonialdetailview", args=[self.slug])
    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
