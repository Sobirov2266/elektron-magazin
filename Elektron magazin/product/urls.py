from django.urls import path
from product import views

urlpatterns = [
    path('<int:id>', views.product_detail, name='product_detail'),
    path('', views.products, name='products'),
]
