from django.http import HttpResponse
# Create your views here.

def homeView(request):
    message = "Hello World"
    return HttpResponse(message)

def aboutView(request):
    message = "This is the desciption for hello world"
    return HttpResponse(message)