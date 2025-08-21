from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from simplefitapi.views.workout_views import WorkoutView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'workouts', WorkoutView, 'workout')

urlpatterns = [
    path('', include(router.urls)),
]
