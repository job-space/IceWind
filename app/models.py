from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class NewsPost(models.Model):
    news_image = models.ImageField(upload_to=f"news_image/%Y/%m/%d/", null=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    news_content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.category_name


class MenuPost(models.Model):
    menu_image = models.ImageField(upload_to=f"menu_image/%Y/%m/%d/", null=False)
    title_menu = models.CharField(max_length=100, null=False, blank=False)
    composition = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    weight = models.IntegerField(null=False, blank=False)

    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return self.title_menu


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)


class Franchise(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)


class Resume(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    file = models.FileField(upload_to="user_resume/%Y/%m/%d/", null=False)
    
