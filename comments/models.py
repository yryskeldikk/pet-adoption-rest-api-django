from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import Account
from django.core.validators import MaxValueValidator, MinValueValidator


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, 
                                     null=True, 
                                     blank=False, 
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    from_user = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.TextField(max_length=4096)
    rating = models.IntegerField(null=True, blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)])
    response = models.ForeignKey('self', null=True, blank=False, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment ({self.id}) by {self.from_user.username} on {self.creation_time}"
