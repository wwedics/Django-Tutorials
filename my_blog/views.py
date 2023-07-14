# from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse("<h1>Home</h1>")
    context = {'name': 'wedics'}
    return render(req, "pages/home.html", context)

def about(req):
    return render(req, "pages/about.html")

def portfolio(req):
    return render(req, "pages/portfolio.html")

def blog(req):
    return render(req, "pages/blog.html")

def contact(req):
    return render(req, "pages/contact.html")