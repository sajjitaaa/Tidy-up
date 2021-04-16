from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
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
        activation_url = "http://localhost:8000/accounts/activate/%s" %(self.activation_key)
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
        send_mail(subject, message, from_email, [self.user.email], **kwargs)
