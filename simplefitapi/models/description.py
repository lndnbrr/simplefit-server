from django.db import models
from .user import User

class Description(models.Model):
    description = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='description_tag', null=False)
