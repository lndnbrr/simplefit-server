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

    def create(self, request):
        """create view for descriptions"""
        user = User.objects.get(pk = request.data['user_id'])
        description = Description.objects.create(
          description = request.data['description'],
          user_id = user
        )
        description.save()

        serialized = DescriptionSerializer(description)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """delete view for descriptions"""
        description = Description.objects.get(pk=pk)
        description.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class DescriptionSerializer(serializers.ModelSerializer):
    """ JSON serializer for descriptions """

    class Meta:

        model= Description
        fields= ('id', 'description', 'user_id')
        depth = 1
