from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from simplefitapi.views.workout_views import WorkoutView
from simplefitapi.views.description_views import DescriptionView
from simplefitapi.views.muscle_group_views import MuscleGroupView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'workouts', WorkoutView, 'workout')
router.register(r'descriptions', DescriptionView, 'description')
router.register(r'muscle_groups', MuscleGroupView, 'muscle_group')

urlpatterns = [
    path('', include(router.urls)),
]
