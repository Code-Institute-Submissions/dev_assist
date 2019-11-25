from django.shortcuts import render, redirect, reverse

def view_cart(request):
    '''A View that renders the cart contents page'''
    context={
        'title':'Cart'
    }
    return render(request, "cart/cart.html", context)

def add_to_cart(request, id):
    '''Add a donation item to the cart'''
    quantity = 1
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view-cart'))

def delete_from_cart(request, id):
    '''function to remove an item from the cart'''
    item_id = id
    cart = request.session.get('cart', {})
    if cart[item_id] > 0:
        cart.pop(item_id)
        request.session['cart'] = cart
    return redirect(reverse('view-cart'))