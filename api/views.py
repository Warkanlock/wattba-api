from rest_framework import generics

from . import models, serializers
from .search import *


class HomeView(generics.ListCreateAPIView):
    #taylor the content
	queryset = models.Lesson.objects.all()
	serializer_class = serializers.LessonSerializer


class UserList(generics.ListCreateAPIView):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.User.objects.all()
	lookup_field = 'pk'
	serializer_class = serializers.UserSerializer

class UserCreate(generics.ListCreateAPIView):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserCreateSerializer


class LessonsList(generics.ListCreateAPIView):
	queryset = models.Lesson.objects.all()
	serializer_class = serializers.LessonSerializer

class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Lesson.objects.all()
	lookup_field = 'pk'
	serializer_class = serializers.LessonSerializer

class SubjectsList(generics.ListCreateAPIView):
	queryset = models.Subject.objects.all()
	serializer_class = serializers.SubjectSerializer

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Subject.objects.all()
	lookup_field = 'pk'
	serializer_class = serializers.SubjectSerializer

	# this relation allows use to determine which teacher is teaching which subject at which level

class SubjectTeachingDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.SubjectTeaching.objects.all()
	lookup_field = 'pk'
	serializer_class = serializers.SubjectTeachingSerializer

class SubjectTeachingCreate(generics.CreateAPIView):
	queryset = models.SubjectTeaching.objects.all()
	serializer_class = serializers.SubjectTeachingSerializer

class SearchView(generics.ListAPIView):
	lookup_field = 'slug'
	serializer_class = serializers.LessonSerializer

	def get_queryset(self):
		lookup_field = self.kwargs['slug']
		pk_list = search_title(lookup_field, [])
		pk_list += search_content(lookup_field, pk_list)
		pk_list += search_summary(lookup_field, pk_list)
		pk_list += search_tags(lookup_field, pk_list)
		queryset =  models.Lesson.objects.filter(pk__in=pk_list)
		return queryset
    