from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.

role_choices = (
    ('ad', 'admin'),
    ('rg', 'regular')
)


class Team(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list

    email = models.EmailField()
    role = models.CharField(choices=role_choices, max_length=10)

