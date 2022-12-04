from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user

# Create your views here.
import armor.products.models
from armor.products.models import Product


class ProductsList(views.ListView):
    template_name = 'products/list.html'
    model = Product


class ProductDetailsView(views.DetailView):
    template_name = 'products/details.html'
    model = Product


class CreateProductView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Product
    template_name = 'products/create.html'

    fields = ('name', 'description', 'image', 'price', 'user')

    def get_success_url(self):
        return reverse_lazy('index')
