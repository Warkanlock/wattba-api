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
	get_teachers = serializers.ReadOnlyField()
	class Meta:
		model = models.Subject
		fields = ('id', 'name', 'get_lessons', 'get_teachers' )


class LessonSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Lesson
		fields = ('id', 'title', 'content', 'subject', 'author', 'grade', 'tags', 'bookmarked')


class SubjectTeachingSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.SubjectTeaching
		fields = ('id', 'teacher', 'subject', 'grade')