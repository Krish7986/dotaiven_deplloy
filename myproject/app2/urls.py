

from django.urls import path
from app2 import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.product, name="products"),
    path("product/<int:id>/", views.product, name="product"),
]
