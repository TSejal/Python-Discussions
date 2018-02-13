from rest_framework import serializers
from discussion.models import *


class listDiscssionsserializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion

# class validateListDiscssionsSerializer(serializers.Serializer):
#     title = serializers.CharField(required=False)


class addCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
 
