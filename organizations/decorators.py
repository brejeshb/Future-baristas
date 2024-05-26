from django.shortcuts import redirect


def unauthenticated_user(view_func):
    """
    Decorator to redirect logged-in users away from specific views.
    """

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")  # Redirect to the index page if user is logged in
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
