from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from simplefitapi.views.workout_views import WorkoutView
from simplefitapi.views.description_views import DescriptionView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'workouts', WorkoutView, 'workout')
router.register(r'descriptions', DescriptionView, 'description')

urlpatterns = [
    path('', include(router.urls)),
]
