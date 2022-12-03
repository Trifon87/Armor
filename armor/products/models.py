from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class Product(models.Model):
    slug = models.SlugField(editable=False, allow_unicode=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='products',
    )

    price = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
