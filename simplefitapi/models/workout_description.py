from django.db import models
from .workout import Workout
from .description import Description

class WorkoutDescription(models.Model):
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='workout_description')
    description_id = models.ForeignKey(Description, on_delete=models.CASCADE, related_name='workout_description')
