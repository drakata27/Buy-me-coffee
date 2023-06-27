import stripe
import os
from django.shortcuts import redirect, render
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')

stripe.api_key=settings.STRIPE_SECRET_KEY

def checkout(request):
    DOMAIN = 'http://' + os.getenv('HOST_AND_PORT') + '/'
    checkout_session = stripe.checkout.Session.create(
    line_items=[
        {
            'price': 'price_1NNbhHKEjjyTT4MxuTnZXNj8',
            'quantity': 1,
        },
    ],
    mode='payment',
    success_url=DOMAIN + 'success',
    cancel_url=DOMAIN + 'cancel',
    )
    return redirect(checkout_session.url, code=303)