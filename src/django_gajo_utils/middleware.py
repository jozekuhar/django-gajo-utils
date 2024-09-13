
# request timing
# sql queries 

class GajoUtilsMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        print(request)
        response = self.get_response(request)
        print(response)
        print('hecko')
        print('hey may')
        return response
