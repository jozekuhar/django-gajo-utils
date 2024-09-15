import functools
import time

from .utils import pretty_print


def stats(func):
    @functools.wraps(func)
    def wrapper(request, /, *args, **kwargs):
        t1 = time.perf_counter_ns()
        result = func(request, *args, **kwargs)
        t2 = time.perf_counter_ns()
        pretty_print("Function time", f"{(t2 - t1) / 1_000_000}ms")
        return result

    return wrapper
