from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def bestseller(request):
    return render(request, 'bestseller.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')
def single(request):
    return render(request, 'single.html')


def custom_404(request, exception):
    # Bạn có thể truyền context nếu cần
    context = {}
    return render(request, "404.html", context=context, status=404)