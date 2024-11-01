from django.urls import path
from .views import CartViews

urlpatterns = [
    path('cart-items/', CartViews.as_view()),
    path('cart-items/<int:id>', CartViews.as_view()),
]
