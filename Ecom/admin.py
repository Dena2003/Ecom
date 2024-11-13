from django.contrib import admin

# Register your models here.
from . models import Product

#Registering the models Created

admin.site.register(Product)