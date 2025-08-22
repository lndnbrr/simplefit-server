from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from simplefitapi.models import Workout

class WorkoutView(ViewSet):

    def list(self, request):
        """list view for workouts"""
        workouts = Workout.objects.all()

        user = self.request.query_params.get('user_id_id', None)
        name = self.request.query_params.get('name', None)

        if name is not None:
            workouts = workouts.filter(name=name)

        if user is not None:
            workouts = workouts.filter(user_id_id=user)

        serialized = WorkoutSerializer(workouts, many=True)
        return Response(serialized.data)

class WorkoutSerializer(serializers.ModelSerializer):
    """ JSON serializer for workouts """
    class Meta:
        model = Workout
        fields = ('id', 'name', 'num_of_sets', 'total_reps', 'max_weight', 'time_stamp', 'is_complete', 'muscle_group_id', 'user_id')
        depth = 1
