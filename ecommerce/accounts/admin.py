from django.contrib import admin
from .models import UserStripe, EmailConfirmed, UserAddress, UserDefaultAddress
# Register your models here.
admin.site.register(UserStripe)
admin.site.register(EmailConfirmed)
admin.site.register(UserAddress)
admin.site.register(UserDefaultAddress)
