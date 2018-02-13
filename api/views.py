from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import  authentication_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from discussion.models import *
from discussion.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class ListDiscussions(APIView):
	def get(self, request, format=None):
		discussion_list = Discussion.objects.filter(discussion_type__in = ['article', 'question'])
		serializer = listDiscssionsserializer(discussion_list, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)



@authentication_classes((TokenAuthentication,))
class CreateCommentClass(APIView):
	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		print request.user
		if request.user.is_authenticated():
			owner = request.user
			data = request.data
			data['added_by'] = owner.id
			serializer = addCommentSerializer(data=data)
			if serializer.is_valid():
				discussion_id = request.data['discussion']
				comment = Comment.objects.all().filter(discussion=discussion_id, added_by=owner.id).exists()
				if comment == True:
					return Response({'error': 'You already commented on this Discussion.'}, status=status.HTTP_200_OK)
				else:
					obj = Discussion.objects.get(id=discussion_id)
					dis_list = Comment.objects.filter(added_by=owner.id)
					print obj
					print dis_list
					if obj in dis_list:
						return Response({'error': 'You can not comment on your own Discussion.'}, status=status.HTTP_200_OK)
					else:
						serializer.save()
						return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


class SearchDiscussions(APIView):
    def get(self, request, format=None):
		text = request.GET.get('text')
		title = request.GET.get('title')
		discussion_type = request.GET.get('discussion_type')
		search_detail = Discussion.objects.filter(Q(title__icontains=title) & Q(text__icontains=text) & Q(discussion_type__icontains=discussion_type))  
		# search_detail = Discussion.objects.filter(title__icontains=title,text__icontains = text,discussion_type__icontains = discussion_type)
		data = listDiscssionsserializer(search_detail, many=True)
		return Response(data.data, status=status.HTTP_200_OK)



   