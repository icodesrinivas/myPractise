def my_middleware(get_response):

    def my_function(request):
        # Write code before view execution
        response = get_response(request)
        # Write code after view execution
        return response
    return my_function

class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Write code before view execution
        response = self.get_response(request)
        # Write code after view execution
        return response