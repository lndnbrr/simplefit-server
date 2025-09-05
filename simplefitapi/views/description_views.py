from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplefitapi.models import Description

class DescriptionView(ViewSet):

    def list(self, request):
        """list view for descriptions"""
        descriptions = Description.objects.all()

        uid = self.request.query_params.get('uid', None)

        if uid is not None:
            descriptions = descriptions.filter(uid = uid)

        serialized = DescriptionSerializer(descriptions, many=True)
        return Response(serialized.data)

    def create(self, request):
        """create view for descriptions"""
        description = Description.objects.create(
          description = request.data['description'],
          uid = request.data['uid'],
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
        fields= ('id', 'description', 'uid')
        depth = 1
