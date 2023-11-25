from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import Account

class Notifications(models.Model):
    TYPES = (
        ('new_comment', 'New Comment'),
        ('new_application', 'New application'),
        ('status_update', 'Status update')
    )

    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=512)
    read = models.BooleanField(default=False)
    action_link = models.CharField(max_length=256)
    type = models.CharField(max_length=50, choices=TYPES)
    content_type = models.ForeignKey(ContentType, 
                                     null=True, 
                                     blank=True, 
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')