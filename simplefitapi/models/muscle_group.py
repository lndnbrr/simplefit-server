from django.db import models

class MuscleGroup(models.Model):
    muscle_group = models.CharField(max_length=50)
