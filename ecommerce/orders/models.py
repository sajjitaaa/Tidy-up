from django.db import models
from carts.models import Cart
from django.conf import settings
from decimal import Decimal
from accounts.models import UserAddress

# Create your models here.

settings.AUTH_USER_MODEL

STATUS_CHOICES = (
        ("Started", "Started"),
        ("Abandoned", "Abandoned"),
        ("Finished", "Finished"),
        )

try:
    tax_rate = settings.DEFAULT_TAX_RATE
except Exception:
    raise NotImplementedError()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.0, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    order_id = models.CharField(max_length=120, unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    shipping_address = models.ForeignKey(UserAddress, related_name="shipping_address", default=1, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(UserAddress, related_name="billing_address", default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id

    def get_final_amount(self):
        instance = Order.objects.get(id=self.id)
        tax_rate_dec = "%s" % (tax_rate)
        instance.tax_total = Decimal(tax_rate_dec) * Decimal(self.sub_total)
        instance.final_total = Decimal(self.sub_total) + Decimal(instance.tax_total)
        instance.save()
        return self.final_total
