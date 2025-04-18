from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.urls import reverse
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def myview(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        return redirect('unauthorized')
    return myview