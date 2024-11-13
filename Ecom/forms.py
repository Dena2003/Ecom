from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Importing the Product model

from .models import Product

#Creating a DjangoForm for storing productdetails

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'image', 'price', 'details']

#Creating a Django Form for Authentication Purpose
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
        'username': 'Username',
        'email': 'Email Address',
        'password1': 'Password',
        'password2': 'Confirm Password',
    }
      