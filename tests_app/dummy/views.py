from django.http import HttpResponse


def simple_endpoint(request):
    return HttpResponse()


def simple_endpoint_with_cookies(request):
    response = HttpResponse()
    response.set_cookie("cookie", "cookie_value")
    return response


def simple_endpoint_with_content(request):
    return HttpResponse("simple content")
