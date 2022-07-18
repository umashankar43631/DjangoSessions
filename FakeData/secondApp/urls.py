from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('loadProducts/', views.load_products, name="Data"),
    path('product/<int:id>', views.product, name="product")
]