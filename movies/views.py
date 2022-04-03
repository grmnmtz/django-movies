from django.http import HttpResponse


from django.http import HttpResponse

def movies(request):
    return HttpResponse("Hello there")

def home(request):
    return HttpResponse("Home page")