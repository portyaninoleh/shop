from functools import wraps

from django.http import HttpResponseBadRequest


def ajax_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.is_ajax():
            return func(request, *args, **kwargs)
        return HttpResponseBadRequest()

    return wrapper
