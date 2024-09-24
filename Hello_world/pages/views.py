from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
# Create your views here.

def aboutView(request):
    # template_name  = "about.html"
    return render(request, 'about.html')

class ContactView(TemplateView):
    template_name = "contact.html"

class CartView(TemplateView):
    template_name = "cart.html"


class HomeView(TemplateView):
    template_name = 'index.html'
