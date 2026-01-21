from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'user_app/home.html')

#register user
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.warning(request, "Passwords do not match!")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists!")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.warning(request, "email already exists!")
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration Successful! Please Login.")
        return redirect('login')

    return render(request, 'user_app/register.html')

#user login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                messages.success(request, "Login Successful")
                return redirect('/admin/')
            else:
                messages.success(request, "Login Successful")
                return redirect('home')
        else:
            messages.warning(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'user_app/login.html')


#user logout
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('home')

#view products list
def products(request):
    products = Product.objects.all()
    return render(request, 'user_app/products.html', {'products': products})

#view product details
def product_details(request, id):
    product=Product.objects.get(id=id )
    return render(request, 'user_app/product_details.html',{ 'product':product })



#user dashboard
@login_required(login_url='user_login')
def user_dashboard(request):
    products = Product.objects.all()
    return render(request, 'user_app/userDashboard.html', {'products': products})

#add to cart
@login_required(login_url='login')
def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

#view cart
@login_required(login_url='login')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total=0
    for item in cart_items:
        total+=item.subtotal
    return render(request, 'user_app/cart.html', {'cart_items': cart_items , 'total':total})

#update cart
@login_required(login_url='login')
def increase_quantity(request, item_id):
    item=CartItem.objects.get(id=item_id ,user=request.user)
    item.quantity+=1
    item.save()
    return redirect('cart')

@login_required(login_url='login')
def decrease_quantity(request, item_id):
    item=CartItem.objects.get(id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity-=1
        item.save()
    else:
        item.delete()
    return redirect('cart')

#remove from cart
@login_required(login_url='login')
def remove_from_cart(request, item_id):
    item=CartItem.objects.get(id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

#checkout
@login_required(login_url='login')
def checkout(request):
    cart_items=CartItem.objects.filter(user=request.user)
    shipping=50
    tot_amount=sum(item.subtotal for item in cart_items)
    final_amount=tot_amount+shipping
    
    return render(request, 'user_app/checkout.html', {'tot':final_amount ,'shipping':shipping, 'item':cart_items})