from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse

from localflavor.in_.in_states import STATE_CHOICES
# Create your models here.


class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.stripe_id)

#model to track if user has confirmed their email


class EmailConfirmed(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=200)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.confirmed)

    def activate_user_email(self): # instance method
        # send email here and render a string
        activation_url = "%s/%s" %(settings.SITE_URL, reverse("activation_view", args=[self.activation_key]))
        context = {
                    "activation_key": self.activation_key,
                    "activation_url": activation_url,
                    "user": self.user.username,
        }
        message = render_to_string("accounts/activation_message.txt", context)
        subject = "Activate your Email"
        print(message)
        print(self.activation_key)
        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.user.email], kwargs)


class UserAddressManager(models.Manager):
    def get_billing_addresses(self, user):
        return super(UserAddressManager, self).filter(billing=True).filter(user=user)


class UserAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120, choices=STATE_CHOICES, null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=120)
    shipping = models.BooleanField(default=True)
    billing = models.BooleanField(default=True)


    def __str__(self):
        return self.get_address()

    def get_address(self):
        return "%s, %s, %s, %s, %s" %(self.address, self.city, self.state, self.country, self.zipcode)

    objects = UserAddressManager()

    # class Meta:
    #     ordering = ['-timestamp', '-updated']


class UserDefaultAddress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    shipping = models.ForeignKey(UserAddress, null=True, blank=True, related_name="user_address_shipping_default", on_delete=models.CASCADE)
    billing = models.ForeignKey(UserAddress, null=True, blank=True,  related_name="user_address_billing_default",  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)
