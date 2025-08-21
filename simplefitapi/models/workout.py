from django.db import models
from .muscle_group import MuscleGroup
from .user import User

class Workout(models.Model):
    name = models.CharField(max_length=50)
    num_of_sets = models.IntegerField()
    total_reps = models.IntegerField()
    max_weight = models.IntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField()
    muscle_group_id = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE, related_name='workout_log')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_log', null=False)
