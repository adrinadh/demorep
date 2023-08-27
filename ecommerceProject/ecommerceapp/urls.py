from django.urls import path
from . import views

app_name = 'ecommerceapp'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='productByCategory'),
    path('<slug:c_slug>/<slug:product_slug>/',
         views.prodetails, name='productDetails'),
]
