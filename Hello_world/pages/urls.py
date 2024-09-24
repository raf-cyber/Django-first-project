from django.urls import path
from pages.views import homeView, aboutView, contactView, cartView

urlpatterns = [
    path('home/', homeView.as_view()),
    path('about/', aboutView),
    path('contact/', contactView),
    path('cart/', cartView)
]