from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Home page
def home(request):
    # return HttpResponse("<h1>Home page</h1>")
    return render(request, 'pages/home.html', {"page_name": "Home Page"})

# About us
def about(request):
        # return HttpResponse("<h1>About Us Page</h1>")
        return render(request, 'pages/about.html')

# Contact Us
def contact(request):
    # return HttpResponse("<h1>Contact Us Page</h1>")
    return render(request, 'pages/contact.html')

# Services
def services(request):
    # return HttpResponse("<h1>Services Page</h1>")
    return render(request, 'pages/services.html')
