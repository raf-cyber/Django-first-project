from django.urls import path
from pages.views import homeView, aboutView, contactView, cartView, HomeView

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('about/', aboutView),
    path('contact/', contactView),
    path('cart/', cartView)
]