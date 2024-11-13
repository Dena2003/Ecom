from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from django.contrib.auth import authenticate, login ,logout
from .forms import UserRegistrationForm
from .models import Product, Cart, CartItem

#Creating a view for login

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

#Creating a view for home page
def home(request):
    return render(request,'home.html', {'userName' : request.user.username})

#Function for the registration of new users

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

#Creating a view for logout

def logout_user(request):
    logout(request)
    return redirect('login')

#Function for listing the products

def product_list(request):
    #Fetch all the product records from product model
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_list.html', {'products': products, 'form': form})

#Function for creating new products

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_edit.html', {'form': form})
#Function for editing  existing products
def product_edit(request):
    product_name = request.GET.get('product_name')
#Retrieve the product by its name using get_object_or_404,if the product with that name does'nt exist it raises an error

    product = get_object_or_404(Product, product_name=product_name)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_edit.html', {'form': form})

#Function for deleting the products from productlist

def product_delete(request):
    product_name = request.GET.get('product_name')
    product = get_object_or_404(Product, product_name=product_name)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})

#Creating a view for adding cart items to a cart

def add_to_cart(request, product_name):
    #Getting the product using productname

    product = get_object_or_404(Product, product_name=product_name)

    #Getting the cart of current user,if not created creates a new one

    cart, created = Cart.objects.get_or_create(user=request.user)

    #Getting the cartitem of specified cart and product
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')
    
#creating a view for removing cart items from a cart

def remove_from_cart(request, product_name):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, product_name=product_name)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    return redirect('cart_detail')

#Creating a view for displaying the cart details

def cart_detail(request):
    #Getting the cart of current user,if not created creates a new one

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart)

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})



