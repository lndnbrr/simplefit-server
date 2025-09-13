from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from simplefitapi.models import MuscleGroup

class MuscleGroupView(ViewSet):
    def list (self, request):
        """list view for muscle groups"""

        muscle_group = MuscleGroup.objects.all()
        serialized = MuscleGroupSerializer(muscle_group, many = True)
        return Response(serialized.data)

    def retrieve(self, request, pk):
        """retrieve view for muscle groups"""

        muscle_group = MuscleGroup.objects.get(pk=pk)
        serialized = MuscleGroupSerializer(muscle_group)
        return Response(serialized.data)

class MuscleGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = MuscleGroup
        fields = ('id', 'muscle_group')
