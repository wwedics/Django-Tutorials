# from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse("<h1>Home</h1>")
    context = {'name': 'Sardor'}
    return render(req, "index.html", context)

def about(req):
    return render(req, "about.html")

def portfolio(req):
    return render(req, "portfolio.html")

def blog(req):
    return render(req, "blog.html")

def contact(req):
    return render(req, "contact.html")