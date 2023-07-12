from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello_world, name="hello_world"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("my_blog", views.my_blog, name="my_blog"),
    path("project", views.project, name="project"),
    path("contact", views.contact, name="contact"),
]