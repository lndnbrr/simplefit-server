from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
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

    def create(self, request):
        """create view for a user"""
        user = User.objects.create(
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            email = request.data['email'],
            bio = request.data['bio'],
            create_date = request.data['create_date'],
            num_of_logged_workouts = request.data['num_of_logged_workouts'],
            uid = request.data['uid']
        )
        user.save()
        serialized = UserSerializer(user)
        return Response(serialized.data, status= status.HTTP_201_CREATED)

    def update(self, request, pk):
        """update view for a user"""
        user = User.objects.get(pk=pk)
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        user.bio = request.data['bio']
        user.num_of_logged_workouts = request.data['num_of_logged_workouts']
        user.save()
        serialized = UserSerializer(user)
        return Response(serialized.data, status=status.HTTP_200_OK)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'bio', 'create_date', 'num_of_logged_workouts', 'uid')
