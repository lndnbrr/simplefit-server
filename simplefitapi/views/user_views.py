from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response  import Response
from simplefitapi.models import User

class UserView (ViewSet):
    """list view for users"""
    def list(self, request):
        user = User.objects.all()
        serialized = UserSerializer(user, many = True)
        return Response(serialized.data)

    def retrieve(self, request, pk):
        """retrieve view for a single user"""
        user = User.objects.get(pk=pk)
        serialized = UserSerializer(user)
        return Response(serialized.data)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'bio', 'create_date', 'num_of_logged_workouts', 'uid')
