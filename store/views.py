
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product


# HOME PAGE
def home(request):

    return render(
        request,
        'home.html'
    )


# LOGIN PAGE
def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:

            user_obj = User.objects.get(email=email)

            username = user_obj.username

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                next_url = request.GET.get('next')

                if next_url:
                    return redirect(next_url)

                return redirect('dashboard')

            else:

                messages.error(
                    request,
                    "Invalid Email or Password"
                )

        except:

            messages.error(
                request,
                "Invalid Email or Password"
            )

    return render(
        request,
        'login.html'
    )


# LOGOUT
def logout_view(request):

    logout(request)

    return redirect('/')


# REGISTER PAGE
def register_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Account created successfully"
        )

        return redirect('login')

    return render(
        request,
        'register.html'
    )


# CART PAGE
@login_required(login_url='login')
def cart(request):

    cart_items = request.session.get('cart', [])

    total = 0

    for item in cart_items:

        total += item['price']

    return render(
        request,
        'cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )



# ADD TO CART 

@login_required(login_url='login')
def add_to_cart(request, product_id):

    products_data = {

        1: {
            'id': 1,
            'name': 'Crimson Dreams',
            'price': 1499,
            'quantity': 1
        },

        2: {
            'id': 2,
            'name': 'Cyber Silence',
            'price': 2299,
            'quantity': 1
        },

        3: {
            'id': 3,
            'name': 'Ocean Echo',
            'price': 1999,
            'quantity': 1
        }

    }

    cart = request.session.get('cart', [])

    product = products_data.get(product_id)

    if product:

        cart.append(product)

    request.session['cart'] = cart

    return redirect('cart')

    # ADD PRODUCT DATA
    cart.append(products_data[product_id])

    request.session['cart'] = cart

    return redirect('cart')





# CHECKOUT PAGE

@login_required(login_url='login')
def checkout(request):

    cart_items = request.session.get('cart', [])

    cart_total = 0

    for item in cart_items:

        price = float(item.get('price', 0))
        quantity = int(item.get('quantity', 1))

        cart_total += price * quantity

    shipping = 99

    final_total = cart_total + shipping

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'shipping': shipping,
        'final_total': final_total,
    }

    return render(request, 'checkout.html', context)



# PAYMENT PAGE
@login_required(login_url='login')
def payment(request):

    cart = request.session.get('cart', [])

    total_amount = 0

    for item in cart:

        price = float(item.get('price', 0))
        quantity = int(item.get('quantity', 1))

        total_amount += price * quantity

    shipping = 99

    final_total = total_amount + shipping

    return render(
        request,
        'payment.html',
        {
            'total_amount': final_total
        }
    )

# SUCCESS PAGE
@login_required(login_url='login')
def success(request):

    return render(
        request,
        'success.html'
    )


# MY ORDERS PAGE
@login_required(login_url='login')
def my_orders(request):

    return render(
        request,
        'my_orders.html'
    )


# ADMIN DASHBOARD
@login_required(login_url='login')
def admin_dashboard(request):

    return render(
        request,
        'admin_dashboard.html'
    )

def clear_cart(request):

    request.session['cart'] = []

    return redirect('home')


#PRIVAYCY AND POLICY 
def privacy(request):
    return render(request, 'privacy.html')

def contact(request):
    return render(request, 'contact.html')

def terms(request):
    return render(request, 'terms.html')

def refund(request):
    return render(request, 'refund.html')