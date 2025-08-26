from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplefitapi.models import Description, User

class DescriptionView(ViewSet):

    def list(self, request):
        """list view for descriptions"""
        descriptions = Description.objects.all()

        user = self.request.query_params.get('user_id_id', None)

        if user is not None:
            descriptions = descriptions.filter(user_id_id = user)

        serialized = DescriptionSerializer(descriptions, many=True)
        return Response(serialized.data)

    def create(self,request):
        """list view for descriptions"""
        user = User.objects.get(pk = request.data['user_id_id'])
        description = Description.objects.create(
          description = request.data['description'],
          user_id = user
        )
        description.save()

        serialized = DescriptionSerializer(description)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

class DescriptionSerializer(serializers.ModelSerializer):
    """ JSON serializer for descriptions """

    class Meta:

        model= Description
        fields= ('id', 'description', 'user_id')
        depth = 1
