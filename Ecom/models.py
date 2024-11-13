from django.db import models
from django.contrib.auth.models import User

# Creating a model Product for storing the product details
class Product(models.Model):

    #Name of the product with maximum length 255
    product_name = models.CharField(max_length=255, unique=True) 

    #Image of the product 

    image = models.ImageField(upload_to='products/', blank=True, null=True)

    #Price of the product with a maximum of 10 digits ,rounded upto 2 decimal places

    price = models.DecimalField(max_digits=10, decimal_places=2)

    #Details of the product

    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product_name

#Creating a model for Cart

class Cart(models.Model):

    #Creating exactly one cart for a particular user by defining OneToOneField
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"

#Creating a model for Cart Items

class CartItem(models.Model):
    #Cart can have many cart items but CartItem should be associated to one cart

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    #Many cartitem can be associated with one product

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.cart.user.username}'s cart"

