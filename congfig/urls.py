from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("my_blog.urls")),
    path("home", include("my_blog.urls")),
    path("about", include("my_blog.urls")),
    path("my_blog", include("my_blog.urls")),
    path("project", include("my_blog.urls")),
    path("contact", include("my_blog.urls")),
]