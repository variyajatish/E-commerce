from django.db import models

# Create your models here.

class Products(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.CharField(max_length=30)
    price = models.FloatField()
    desc = models.CharField(max_length=300)
    categori = models.CharField(max_length=100)
    # using = models.CharField(max_length=100)

class Newlist(models.Model):
    newproduct = models.ImageField(upload_to='images/')
    productname = models.CharField(max_length=30)

class Featuredproducts(models.Model):
    nameproduct = models.CharField(max_length=30)
    newimg = models.ImageField(upload_to='images/')

class Category(models.Model):
    productimg = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    categori = models.CharField(max_length=100)

class Signup(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpass = models.CharField(max_length=100)

class Cart(models.Model):
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    userId = models.ForeignKey(Signup, on_delete=models.CASCADE)
    quantity = models.IntegerField()



    