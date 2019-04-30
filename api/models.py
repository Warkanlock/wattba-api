from django.db import models
from django.contrib.auth.models import AbstractUser, AnonymousUser
from typing import Union

import requests
from djrichtextfield.models import RichTextField

summary_url = 'http://18.236.191.192:3000/summary?action=[action_name]&[parameters]'


class Subject(models.Model):
    name = models.CharField(max_length=280, blank=False, null=False)

    def __str__(self):
        return self.name

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

    def get_teachers(self):
        values = []
        teachings = SubjectTeaching.objects.filter(subject=self)
        for teaching in teachings:
            values.append({"Teacher": teaching.teacher.username,
                           "grade": teaching.grade})
        return values

    # TOD0
    # tags =  DJANGO TAGGABLE MANAGER


class User(AbstractUser):
    profile_picture = models.ImageField(('users'),
                                        upload_to='frontend/public/users/%Y/%m/%d',
                                        blank=True)
    bio = models.CharField(blank=True, null=True, max_length=250)
    region = models.CharField(blank=True, null=True, max_length=250)
    school_name = models.CharField(blank=True, null=True, max_length=250)

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

    def get_subjects_teaching(self):
        values = []
        teachings = SubjectTeaching.objects.filter(teacher=self)

        for teaching in teachings:
            values.append({"Teacher": teaching.teacher.username,
                           "Subject": teaching.subject.name,
                           "grade": teaching.grade})

        return values


#: Helper type for Django request users: either anonymous or signed-in.
RequestUser = Union[AnonymousUser, User]

class Lesson(models.Model):

    title = models.CharField(max_length=280, blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=280, default="", blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(blank=True, null=True)  # this will also help with filtering
    tags = models.TextField(blank=True, null=True)
    bookmarked = models.BooleanField(default=False, blank=True)
    region = models.TextField(blank=True, null=True)
    supplies = models.TextField(blank=True, null=True)
    # at the moment these are just basic stags separated by commas
    # django taggit is a bit tricky and not worth it atm

    def save(self, *args, **kwargs):
        content = kwargs.get('content')
        # create a summary using the content
        # make an http request
        # from django.conf import settings

        post_data = {"text": content}     # a sequence of two element tuples
        result = requests.post(
            "http://18.236.191.192:3000/summary",
            json=post_data,
        )
        summary = result.json()['result']
        if not len(summary) > 0:
            self.summary = summary

        super(Lesson, self).save(*args, **kwargs)

    def __init__(self, *args, **kwargs):

        sub_val = kwargs.get('subject')
        if type(sub_val) == str:
            # the subject username is being used
            subjects = Subject.objects.filter(name=sub_val)
            if subjects.exists():
                subject = subjects[0]
                kwargs['subject'] = subject
            else:
                new_subject = Subject.objects.create(name=sub_val)
                new_subject.save()
                kwargs['subject'] = new_subject
            super(Lesson, self).__init__(*args, **kwargs)

        super(Lesson, self).__init__(*args, **kwargs)


class SubjectTeaching(models.Model):
    '''
    a teacher can choose to say that they teach which subject at which grade
    This will allow us to tune content for them
    '''
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = grade = models.IntegerField()
