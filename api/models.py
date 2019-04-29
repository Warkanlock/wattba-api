from django.db import models
from django.contrib.auth.models import AbstractUser, AnonymousUser
from typing import Union
from djrichtextfield.models import RichTextField

from taggit.managers import TaggableManager


class Subject(models.Model):
    name = models.CharField(max_length=280, blank=False, null=False)

    def get_lessons(self):

        lessons = Lesson.objects.filter(subject=self)
        values = []
        for lesson in lessons:
            values.append(
                {
                    "title": lesson.title,
                    "content": lesson.content,
                    "author": lesson.author.username,
                    "subject": lesson.subject.name,
                    "grade": lesson.grade,
                    "tags": lesson.tags
                }
            )
        return values
    
        def __str__(self):
            return self.name

    # TOD0
    # tags =  DJANGO TAGGABLE MANAGER


class User(AbstractUser):
    profile_picture = models.ImageField(('users'),
                                        upload_to='frontend/public/users/%Y/%m/%d',
                                        blank=True)
    bio = models.CharField(blank=True, null=True, max_length=250)
    region = models.CharField(blank=True, null=True, max_length=250)
    school_name = models.CharField(blank=True, null=True, max_length=250)
    subjects = models.ManyToManyField(Subject)

    # TODO
    # liked_lessons = models.ManyToManyField(Lesson)
    def __str__(self):
        return self.username

    def get_authored_lessons(self):
        lessons = Lesson.objects.filter(author_id=self.pk)
        values = []
        for lesson in lessons:
            values.append(
                {
                    "title": lesson.title,
                    "content": lesson.content,
                    "author": lesson.author.username,
                    "subject": lesson.subject.name,
                    "grade": lesson.grade,
                    "tags": lesson.tags,
                }
            )
        return values

    def get_liked_lessons(self):
        return self.liked_lessons.values_list(flat=True)

    def get_subjects_following(self):
        values = []
        for pk in self.subjects.all():
            subject = Subject.objects.get(pk=pk.pk)
            values.append({"pk": subject.pk, "name": subject.name})

        return values


#: Helper type for Django request users: either anonymous or signed-in.
RequestUser = Union[AnonymousUser, User]


class Tag(models.Model):
    """Tag for data. Every tag has unique text.
    Tags are intersubject so don't attach them to subjects
    """
    text = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return 'tag'.format(
            tag=self.text)

class Lesson(models.Model):

    title = models.CharField(max_length=280, blank=False, null=False)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=280, blank=False, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField() # this will also help with filtering
    tags = models.TextField()


class SubjectTeaching(models.Model):
    '''
    a teacher can choose to say that they teach which subject at which grade
    This will allow us to tune content for them
    '''
    teacher  =  models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = grade = models.IntegerField()