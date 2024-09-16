from django.http import HttpResponse

from gajo_utils.decorators import timeview
from .models import Product


def endpoint(request):
    return HttpResponse()


def endpoint_with_cookies(request):
    response = HttpResponse()
    response.set_cookie("cookie", "cookie_value")
    return response


def endpoint_with_content(request):
    return HttpResponse("simple content")


def endpoint_with_single_query(request):
    qs = Product.objects.all()
    return HttpResponse(qs)


def endpoint_with_all_products_query(request):
    qs = Product.objects.all()
    return HttpResponse(qs)


def endpoint_with_all_products_query_without_prefetch(request):
    qs = Product.objects.all()

    for product in qs:
        list(product.variants.all())

    return HttpResponse(qs)


def endpoint_with_all_products_query_with_prefetch(request):
    qs = Product.objects.prefetch_related("variants")

    for product in qs:
        list(product.variants.all())

    return HttpResponse(qs)


@timeview
def endpoint_with_timeview_decorator(request):
    return HttpResponse("endpoint")
