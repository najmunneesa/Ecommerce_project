from django.db import models
from django.contrib.auth.models import User
from admin_app.models import *



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
    @property
    def subtotal(self):
        return self.product.price * self.quantity

