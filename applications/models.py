from django.db import models
from accounts.models import Account
from listings.models import Pet
# Create your models here.
class Applications(models.Model):
    STATUSES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('denied', 'Denied'),
        ('withdrawn','Withdrawn')
    )
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    applicant = models.ForeignKey(Account,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUSES, default='pending')