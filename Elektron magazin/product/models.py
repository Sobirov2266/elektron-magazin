from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    name = models.CharField(max_length=150)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    def imageURL(self):
        if self.image:
            return self.image.url
        return ''
