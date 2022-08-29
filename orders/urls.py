from django.urls import path

from . import views


app_name = "orders"
urlpatterns = [
    path('', views.ProductListView.as_view(), name="list"),
    path('<int:pk>/', views.ProductDetailView.as_view(), name="detail"),
    path('cart/', views.cart_view, name="cart"),
    path('checkout/', views.checkout_view, name="checkout"),

    path('update_cart/', views.update_cart, name="update_cart"),
    path('process_order/', views.process_order, name="process_order"),
]
