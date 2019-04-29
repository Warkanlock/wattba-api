from . import models

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

	get_subjects_following= serializers.ReadOnlyField()
	get_authored_lessons = serializers.ReadOnlyField()
	class Meta:
		model = models.User
		fields = ('id', 'username', 'email','profile_picture', 'bio', 'first_name', 'last_name',
		'get_subjects_following', 'get_authored_lessons')


class UserCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.User
		fields = ('id', 'username')


class SubjectSerializer(serializers.ModelSerializer):

	get_lessons = serializers.ReadOnlyField()

	class Meta:
		model = models.Subject
		fields = ('id', 'name', 'get_lessons' )

class LessonSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Lesson
		fields = ('id', 'title', 'content', 'summary', 'subject')
