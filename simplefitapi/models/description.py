from django.db import models

class Description(models.Model):
    description = models.CharField(max_length=50)
    uid = models.CharField(max_length=50, unique=False)
