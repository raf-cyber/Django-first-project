from django.urls import path
from pages.views import aboutView, ContactView, CartView
from pages.views import HomeView 

urlpatterns = [
    path('about/', aboutView),
    path('contact/', ContactView.as_view()),
    path('cart/', CartView.as_view()),
    path('', HomeView.as_view()),
]