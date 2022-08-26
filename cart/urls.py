from django.urls import path
from . import views

urlpatterns=[
    path('cartdetails',views.cart_details,name='cartdetails'),
    path('addcart/<int:product_id>',views.add_cart,name='add_cart'),
    path('delete/<int:product_id>',views.delete_cart,name='deletecart'),
    path('min/<int:product_id>',views.min_cart,name='min_cart'),
]
