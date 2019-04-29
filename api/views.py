from rest_framework import generics

from . import models, serializers


class HomeView(generics.ListCreateAPIView):
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
