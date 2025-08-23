from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from simplefitapi.models import Workout, User, MuscleGroup

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

    def create(self, request):
        """create view for workouts"""

        user = User.objects.get(pk = request.data['user_id'])
        muscle_group = MuscleGroup.objects.get(pk = request.data['muscle_group_id'])

        workout = Workout.objects.create(
            name = request.data['name'],
            num_of_sets = request.data['num_of_sets'],
            total_reps = request.data['total_reps'],
            max_weight = request.data['max_weight'],
            time_stamp = request.data['time_stamp'],
            is_complete = request.data['is_complete'],
            muscle_group_id = muscle_group,
            user_id = user
        )

        serialized = WorkoutSerializer(workout)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

class WorkoutSerializer(serializers.ModelSerializer):
    """ JSON serializer for workouts """
    class Meta:
        model = Workout
        fields = ('id', 'name', 'num_of_sets', 'total_reps', 'max_weight', 'time_stamp', 'is_complete', 'muscle_group_id', 'user_id')
        depth = 1
