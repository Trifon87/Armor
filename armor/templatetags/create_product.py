from django import template
from django.template import Library
from django.urls import reverse_lazy

register = template.Library()


@register.simple_tag
def create_product(user):
    if not user.is_authenticated:
        url = reverse_lazy('create product')
        return f'<a href="{url}"> Create product<a/>'