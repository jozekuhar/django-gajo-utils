import random
import time
from typing import Callable

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from . import config
from .utils import pretty_print


class GajoUtilsMiddleware:
    def __init__(self, get_response: Callable[[WSGIRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> HttpResponse:
        request_id = (
                str(random.randint(0, 9))
                + str(random.randint(0, 9))
                + str(random.randint(0, 9))
                + str(random.randint(0, 9))
                + str(random.randint(0, 9))
        )

        if config.get('REQUEST_COOKIES'):
            pretty_print('Request cookies', request.COOKIES)

        if config.get('REQUEST_DELAY'):
            r1 = time.perf_counter_ns()
            time.sleep(random.uniform(0.05, 0.3))
            r2 = time.perf_counter_ns()
            pretty_print(f'Request delay time #{request_id}',
                         f'{(r2 - r1) / 1_000_000}ms')

        t1: int = 0
        if config.get('REQUEST_TIMER'):
            t1 = time.perf_counter_ns()

        response: HttpResponse = self.get_response(request)

        if config.get('REQUEST_TIMER'):
            t2 = time.perf_counter_ns()
            pretty_print(f'Request actual time #{request_id}:',
                         f'{(t2 - t1) / 1_000_000}ms')

        if config.get('RESPONSE_COOKIES'):
            # raise NotImplementedError('Implement nice representation for response cookies.')
            pretty_print('Response cookies', response.cookies.items())

        if config.get('RESPONSE_CONTENT'):
            pretty_print('Response content', bytes.decode(response.content))

        return response
