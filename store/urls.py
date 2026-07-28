from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'dashboard/',
        views.home,
        name='dashboard'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    # CART
    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    # ADD TO CART
    path(
    'add-to-cart/<int:product_id>/',
    views.add_to_cart,
    name='add_to_cart'
),
    # CHECKOUT
    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    # PAYMENT
    path(
        'payment/',
        views.payment,
        name='payment'
    ),

    # SUCCESS
    path(
        'success/',
        views.success,
        name='success'
    ),

    path(
        'orders/',
        views.my_orders,
        name='my_orders'
    ),

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    
path('privacy/', views.privacy, name='privacy'),
path('contact/', views.contact, name='contact'),
path('terms/', views.terms, name='terms'),
path('refund/', views.refund, name='refund'),

]
