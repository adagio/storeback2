from django.http import HttpResponse

def index(request):
    return HttpResponse("Store. Brands and Products.")

