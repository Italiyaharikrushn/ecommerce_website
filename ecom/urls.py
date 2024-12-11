from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_products, name='show_products'),
    path('add-product/', views.add_product, name='add_product'),
]
