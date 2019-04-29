from rest_framework import generics

from . import models, serializers


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
