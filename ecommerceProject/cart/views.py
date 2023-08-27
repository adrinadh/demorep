from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItems
from ecommerceapp.models import Product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        request.session.create()
        request.session.save()  # Save the session after creation
        cart = request.session.session_key

    return cart


def add_items(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_id = _cart_id(request)

    # Create or retrieve the Cart instance using the cart_id
    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_id)

    # Create or update the CartItems instance
    try:
        cart_item = CartItems.objects.get(cart=cart, product=product)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(
            cart=cart, product=product, quantity=1)

    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_item_queryset=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item_queryset = CartItems.objects.filter(cart=cart, active=True)

        for cart_item in cart_item_queryset:
            total += cart_item.product.price * cart_item.quantity
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', {'total': total, 'counter': counter, 'cart_items': cart_item_queryset})


def remove_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItems.objects.get(product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    else:
        cart_item.delete()

    return redirect('cart:cart_detail')


def delete_items(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItems.objects.get(product=product, cart=cart)

    cart_item.delete()
    return redirect('cart:cart_detail')
