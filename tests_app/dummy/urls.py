from django.urls import path

from . import views

urlpatterns = [
    path(
        "simple/",
        views.simple_endpoint,
        name="simple_endpoint",
    ),
    path(
        "simple-with-cookies/",
        views.simple_endpoint_with_cookies,
        name="simple_endpoint_with_cookies",
    ),
    path(
        "simple-with-content/",
        views.simple_endpoint_with_content,
        name="simple_endpoint_with_content",
    ),
]
