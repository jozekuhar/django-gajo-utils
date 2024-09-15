import pytest

from django.test import Client
from django.urls import reverse


def test_exception_if_debug_is_false(client):
    with pytest.raises(Exception) as error:
        client.get(reverse("simple_endpoint"))

    assert "can only be initialized if DEBUG is True." in str(error)


def test_request_timer_config_enabled(client, settings, capsys):
    settings.DEBUG = True
    setattr(settings, "GAJO_UTILS_CONFIG", {"REQUEST_TIMER": True})

    client.get(reverse("simple_endpoint"))

    assert "Request actual time" in capsys.readouterr().out


def test_request_delay_config_enabled(client, settings, capsys):
    settings.DEBUG = True
    setattr(settings, "GAJO_UTILS_CONFIG", {"REQUEST_DELAY": True})

    client.get(reverse("simple_endpoint"))

    assert "Request delay time" in capsys.readouterr().out


def test_request_cookies_config_enabled(client: Client, settings, capsys):
    settings.DEBUG = True
    setattr(settings, "GAJO_UTILS_CONFIG", {"REQUEST_COOKIES": True})

    client.cookies["cookie"] = "cookie_value"
    client.get(reverse("simple_endpoint"))

    out = capsys.readouterr().out

    assert "Request cookies" in out
    assert "cookie_value" in out


def test_response_cookies_config_enabled(client: Client, settings, capsys):
    settings.DEBUG = True
    setattr(settings, "GAJO_UTILS_CONFIG", {"RESPONSE_COOKIES": True})

    client.get(reverse("simple_endpoint_with_cookies"))

    out = capsys.readouterr().out

    assert "Response cookies" in out
    assert "cookie_value" in out


def test_response_content_config_enabled(client: Client, settings, capsys):
    settings.DEBUG = True
    setattr(settings, "GAJO_UTILS_CONFIG", {"RESPONSE_CONTENT": True})

    res = client.get(reverse("simple_endpoint_with_content"))

    assert "simple content" in str(res.content)
    assert "simple content" in capsys.readouterr().out
