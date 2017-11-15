from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "my_site/index.html")

def products(request):
    return render(request, "my_site/products.html")

def contact(request):
    return render(request, "my_site/contact.html")

def login(request):
    return render(request, "my_site/login.html")

def registered(request):
    return render(request, "my_site/registered.html")

def single(request):
    return render(request, "my_site/single.html")

def faq(request):
    return render(request, "my_site/faq.html")