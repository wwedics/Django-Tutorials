from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View  # import working for only this class
# from django.http import HttpResponse 
from .models import *

def home(req):
    branche = Branche.objects.all()
    context = {
        "branche":branche
        }
    return render(req,"pages/home.html",context)

def our_story(req):
    branche = Branche.objects.all()
    context = {
        "branche":branche
        }
    return render(req,"pages/our_story.html",context)

def service(req):
    branche = Branche.objects.all()
    context = {
        "branche":branche
        }
    return render(req,"pages/service.html",context)

def price_list(req):
    branche = Branche.objects.all()
    price = Price.objects.all()
    context = {
        "branche":branche,
        "price":price,
        }
    return render(req,"pages/price_list.html",context)

# def contact(req):
#     contact = Contact.objects.all()
#     branche = Branche.objects.all()
#     context = {
#         "contact":contact,
#         "branche":branche,
#         }
#     return render(req,"pages/contact.html",context)

def base(req):
    branche = Branche.objects.all()
    context = {
        "branche":branche
        }
    return render(req,"base.html",context)


    # class ContactView(View):
    #     def get(self, request):
    #         return HttpResponse("result")

class ContactView(TemplateView):
    template_name = 'pages/contact.html'


    # It's not working
    # def render_data(self, **kwargs):
    #     context = super(ContactVeiw,self).get_context_data(self, **kwargs)
    #     context = super().get_context_data(**kwargs)
    #     contact = Contact.objects.all()
    #     branche = Branche.objects.all()
    #     context = {
    #     "contact":contact,
    #     "branche":branche,
    #     }

    #     return context


