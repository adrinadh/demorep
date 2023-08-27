from django.urls import path
from .import views


app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_items, name='add_items'),
    path('remove/<int:product_id>/', views.remove_item, name='remove_items'),
    path('delete/<int:product_id>/', views.delete_items, name='delete_items')
]
