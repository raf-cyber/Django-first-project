from django.urls import path
from pages.views import aboutView, ContactView, CartView
from pages.views import HomeView 

urlpatterns = [
    path('about/', aboutView, name = "about"),
    path('contact/', ContactView.as_view(), name = "contact"),
    path('cart/', CartView.as_view(), name = "cart"),
    path('', HomeView.as_view()),
]