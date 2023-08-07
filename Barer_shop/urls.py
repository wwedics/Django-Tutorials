from django.urls import path
from .views import *

urlpatterns = [
    path("", base, name="base"),
    path("home/", home, name="home"),
    path("our_story/", our_story, name="our_story"),
    path("service/", service, name="service"),
    path("price_list/", price_list, name="price_list"),
    path("contact/", ContactView.as_view(), name="contact"),
]