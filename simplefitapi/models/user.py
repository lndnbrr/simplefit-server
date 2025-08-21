from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField(max_length=300)
    create_date = models.DateTimeField(auto_now_add=True)
    num_of_logged_workouts = models.IntegerField()
    uid = models.CharField(max_length=50, unique=True)
