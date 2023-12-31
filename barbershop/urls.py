from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("story/", views.story, name="story"),
    path('services/', views.services, name="services"),
    path('/', views., name=""),
    path('contact/', views.contact, name="contact"),
]
