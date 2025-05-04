from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RL54WJqyArePMNy8Vf1mJ9q5AHIes9SWroh27LxqKuhnKvFtKelEeUBw2vCCrt1EEEvaWEXOhnv0HNIulB05m5B00ooHqoo0n',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
