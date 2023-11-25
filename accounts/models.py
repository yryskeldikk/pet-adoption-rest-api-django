from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class Account(AbstractUser):

    phone_message = 'Phone number must be valid phone number!' 
    phone_regex = RegexValidator(
        regex=r'^[0-9]*$',
        message=phone_message
    )

    location = models.CharField(max_length = 256)
    phone_number = models.CharField(validators=[phone_regex], max_length=11) 
    isShelter = models.BooleanField(default=False) # default register as Pet Seeker
    avatar = models.ImageField(default='blank-profile.png', upload_to='media')
