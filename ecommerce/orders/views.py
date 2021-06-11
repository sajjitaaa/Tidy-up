import time
import stripe
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from carts.models import Cart
from .models import Order
from .utils import id_generator
from accounts.forms import UserAddressForm
from accounts.models import UserAddress
from django.conf import settings
from django.contrib import messages

# Create your views here.

try:
    stripe_pub = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret = settings.STRIPE_SECRET_KEY
except Exception:
    raise NotImplementedError()


stripe.api_key = stripe_secret

def orders(request):
    context = {}
    template = 'orders/user.html'
    return render(request, template, context)


@login_required
def checkout(request):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id=None
        return HttpResponseRedirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart=cart)
        # print("try")
    except Order.DoesNotExist:
        new_order = Order(cart=cart)
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
        print(new_order.sub_total)
    except:
        new_order = None
        return HttpResponseRedirect(reverse("cart"))

    final_amount = 0
    if new_order is not None:
        new_order.sub_total = cart.total
        new_order.save()
        final_amount = new_order.get_final_amount()

    try:
        address_added = request.GET.get("address_added")
    except:
        address_added = None

    if address_added is None:
        address_form = UserAddressForm()
    else:
        address_form = None


    current_addresses = UserAddress.objects.filter(user=request.user)
    billing_addresses = UserAddress.objects.get_billing_addresses(user=request.user)

    if request.method == "POST":
        try:
            print("hello try")
            user_stripe = request.user.userstripe.stripe_id
            customer = stripe.Customer.retrieve(user_stripe)
            # print(customer)
        except:
            print("hello except")
            customer = None
        if customer is not None:
            billing_a = request.POST['billing_address']
            shipping_a = request.POST['shipping_address']
            token = request.POST['stripeToken']

            try:
                billing_address_instance = UserAddress.objects.get(id=billing_a)
            except:
                billing_address_instance = None

            try:
                shipping_address_instance = UserAddress.objects.get(id=shipping_a)
            except:
                shipping_address_instance = None


            # card = customer.cards.create(card=token)
            # customer.source = token
            card = stripe.Customer.create_source(
                          customer.stripe_id,
                          source=token,
                        )
            card.address_city = billing_address_instance.city or None
            card.address_line1 = billing_address_instance.address or None
            card.address_line2 = billing_address_instance.address2 or None
            card.address_state = billing_address_instance.state or None
            card.address_zip = billing_address_instance.zipcode or None
            card.address_country = billing_address_instance.country or None
            card.save()

            token = request.POST['stripeToken']
            charge = stripe.Charge.create(
                      amount=int(final_amount*100),
                      currency="inr",
                      card=card,
                      customer=customer,
                      description="Charge is %s" %(request.user.username),
                    )
            print(charge)
            print(card)

            if charge["captured"]:
                new_order.status = "Finished"
                new_order.shipping_address = shipping_address_instance
                new_order.billing_addresses = billing_address_instance
                new_order.save()
                del request.session['cart_id']
                del request.session['items_total']
                messages.success(request, "Your has been completed!")
                return HttpResponseRedirect(reverse("user_orders"))

    #add shipping address
    #add billing address
    #add and return credit card
        # cart.delete()

    context = {"current_addresses": current_addresses, "billing_addresses": billing_addresses, "address_form": address_form, "stripe_pub": stripe_pub, "order": new_order}
    template = 'orders/checkout.html'
    return render(request, template, context)


def payment_view(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id=None
        return HttpResponseRedirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart=cart)
        # print("try")
    except Order.DoesNotExist:
        new_order = Order(cart=cart)
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
        print(new_order.sub_total)
    except:
        new_order = None
        return HttpResponseRedirect(reverse("cart"))

    final_amount = 0
    if new_order is not None:
        new_order.sub_total = cart.total
        new_order.save()
        final_amount = new_order.get_final_amount()

    try:
        address_added = request.GET.get("address_added")
    except:
        address_added = None

    if address_added is None:
        address_form = UserAddressForm()
    else:
        address_form = None


    current_addresses = UserAddress.objects.filter(user=request.user)
    billing_addresses = UserAddress.objects.get_billing_addresses(user=request.user)

    if request.method == "POST":
        try:
            print("hello try")
            user_stripe = request.user.userstripe.stripe_id
            customer = stripe.Customer.retrieve(user_stripe)
            # print(customer)
        except:
            print("hello except")
            customer = None
        if customer is not None:
            billing_a = request.POST['billing_address']
            shipping_a = request.POST['shipping_address']
            token = request.POST['stripeToken']

            try:
                billing_address_instance = UserAddress.objects.get(id=billing_a)
            except:
                billing_address_instance = None

            try:
                shipping_address_instance = UserAddress.objects.get(id=shipping_a)
            except:
                shipping_address_instance = None


            # card = customer.cards.create(card=token)
            # customer.source = token
            card = stripe.Customer.create_source(
                          customer.stripe_id,
                          source=token,
                        )
            card.address_city = billing_address_instance.city or None
            card.address_line1 = billing_address_instance.address or None
            card.address_line2 = billing_address_instance.address2 or None
            card.address_state = billing_address_instance.state or None
            card.address_zip = billing_address_instance.zipcode or None
            card.address_country = billing_address_instance.country or None
            card.save()

            token = request.POST['stripeToken']
            charge = stripe.Charge.create(
                      amount=int(final_amount*100),
                      currency="inr",
                      card=card,
                      customer=customer,
                      description="Charge is %s" %(request.user.username),
                    )
            print(charge)
            print(card)

            if charge["captured"]:
                new_order.status = "Finished"
                new_order.shipping_address = shipping_address_instance
                new_order.billing_addresses = billing_address_instance
                new_order.save()
                del request.session['cart_id']
                del request.session['items_total']
                messages.success(request, "Your has been completed!")
                return HttpResponseRedirect(reverse("user_orders"))

    #add shipping address
    #add billing address
    #add and return credit card
        # cart.delete()

    context = {"stripe_pub": stripe_pub, "order": new_order}
    template = 'orders/payment.html'
    return render(request, template, context)
