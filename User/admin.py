from django.contrib import admin
from .models import Products, Newlist, Featuredproducts, Category, Signup, Cart, Order
# Register your models here.
admin.site.register(Products)
admin.site.register(Newlist)
admin.site.register(Featuredproducts)
admin.site.register(Category)
admin.site.register(Signup)
admin.site.register(Cart)
admin.site.register(Order)
