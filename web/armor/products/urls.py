from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from armor.products import views

urlpatterns = [
    path("", views.ProductsList.as_view(), name='index'),
    path('<int:pk>/<slug:slug>/', views.ProductDetailsView.as_view(), name='product details'),
    path('create/', views.CreateProductView.as_view(), name= 'create product'),
]