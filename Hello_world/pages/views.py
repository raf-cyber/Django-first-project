from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

# def homeView(request):
#     message = "Hello World"
#     return HttpResponse(message)

# def aboutView(request):
#     message = "This is the desciption for hello world"
#     return HttpResponse(message)

# def contactView(request):
#     message="This is a contact page"
#     return HttpResponse(message)

# def cartView(request):
#     message="This is a cart page"
#     return HttpResponse(message)


class HomeView(TemplateView):
    template_name = 'index.html'