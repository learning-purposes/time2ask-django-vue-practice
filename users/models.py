from django.db import models
from django.contrib.auth.models import AbstractUser


# extend the user model, to add fields later
class CustomUser(AbstractUser):
    # adding additional fields, see forms.py
    mobile_number = models.CharField(max_length=10, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.email
