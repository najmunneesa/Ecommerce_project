from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
   
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


