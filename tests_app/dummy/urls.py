from django.urls import path

from . import views

urlpatterns = [
    path(
        "enpoint/",
        views.endpoint,
        name="endpoint",
    ),
    path(
        "endpoint-with-cookies/",
        views.endpoint_with_cookies,
        name="endpoint_with_cookies",
    ),
    path(
        "endpoint-with-content/",
        views.endpoint_with_content,
        name="endpoint_with_content",
    ),
    path(
        "endpoint_with_all_products_query/",
        views.endpoint_with_all_products_query,
        name="endpoint_with_all_products_query",
    ),
    path(
        "endpoint_with_all_products_query_without_prefetch/",
        views.endpoint_with_all_products_query_without_prefetch,
        name="endpoint_with_all_products_query_without_prefetch",
    ),
    path(
        "endpoint_with_all_products_query_with_prefetch/",
        views.endpoint_with_all_products_query_with_prefetch,
        name="endpoint_with_all_products_query_with_prefetch",
    ),
    path(
        "endpoint_with_timeview_decorator/",
        views.endpoint_with_timeview_decorator,
        name="endpoint_with_timeview_decorator",
    ),
]
