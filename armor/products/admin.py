from django.contrib import admin

# Register your models here.
from armor.products.models import Product, Post, Comment


class PostInline(admin.StackedInline):
    model = Post


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')

    inlines = (PostInline,)


admin.site.register(Product, ProductAdmin)
admin.site.register(Post)
admin.site.register(Comment)
