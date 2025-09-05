from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from simplefitapi.models import Workout, MuscleGroup

class WorkoutView(ViewSet):

    def list(self, request):
        """list view for workouts"""
        workouts = Workout.objects.all()

        uid = self.request.query_params.get('uid', None)
        name = self.request.query_params.get('name', None)
        muscle_group = self.request.query_params.get('muscle_group_id_id', None)

        if name is not None:
            workouts = workouts.filter(name=name)

        if uid is not None:
            workouts = workouts.filter(uid=uid)

        if muscle_group is not None:
            workouts = workouts.filter(muscle_group_id_id=muscle_group)

        serialized = WorkoutSerializer(workouts, many=True)
        return Response(serialized.data)

    def create(self, request):
        """create view for workouts"""

        muscle_group = MuscleGroup.objects.get(pk = request.data['muscle_group_id'])

        workout = Workout.objects.create(
            name = request.data['name'],
            num_of_sets = request.data['num_of_sets'],
            total_reps = request.data['total_reps'],
            max_weight = request.data['max_weight'],
            is_complete = request.data['is_complete'],
            muscle_group_id = muscle_group,
            uid = request.data['uid'],
        )

        serialized = WorkoutSerializer(workout)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """update view for workouts"""

        muscle_group = MuscleGroup.objects.get(pk = request.data['muscle_group_id'])
        workout = Workout.objects.get(pk = pk)
        workout.name = request.data['name']
        workout.num_of_sets = request.data['num_of_sets']
        workout.total_reps = request.data['total_reps']
        workout.max_weight= request.data['max_weight']
        workout.is_complete = request.data['is_complete']
        workout.muscle_group_id = muscle_group
        workout.save()

        serialized = WorkoutSerializer(workout)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        """delete view for workouts"""

        workout = Workout.objects.get(pk = pk)
        workout.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class WorkoutSerializer(serializers.ModelSerializer):
    """ JSON serializer for workouts """
    class Meta:
        model = Workout
        fields = ('id', 'name', 'num_of_sets', 'total_reps', 'max_weight', 'time_stamp', 'is_complete', 'muscle_group_id', 'uid')
        depth = 1
