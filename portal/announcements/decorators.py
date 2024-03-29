from django.http import HttpResponsePermanentRedirect


def allowed_users(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if str(request.user) == "AnonymousUser":
                return HttpResponsePermanentRedirect('/announcements')
            group = request.user.role
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponsePermanentRedirect('/announcements')
        return wrapper_func
    return decorator
