from django.db import models
from django.contrib.auth.models import AbstractUser, AnonymousUser
from typing import Union
from djrichtextfield.models import RichTextField

from .search import LessonContentIndex


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

    def get_teachers(self):
        values = []
        teachings = SubjectTeaching.objects.filter(subject=self)
        for teaching in teachings:
            values.append({"teacher": teaching.teacher.username, 
                           "grade": teaching.grade})
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

    title = models.CharField(max_length=280, blank=False, null=False)
    content = RichTextField( default="") # models.TextField(max_length=1000, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=280, default="")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField() # this will also help with filtering
    tags = models.TextField( default="")
    # at the moment these are just basic stags separated by commas
    # django taggit is a bit tricky and not worth it atm
    

    def indexing(self):
        obj = LessonContentIndex(
        meta={'id': self.id},
        content=self.content,
        tags=self.tags ,
        title=self.title,
        summary=self.summary,
        id=self.id
            )
        obj.save()
        return obj.to_dict(include_meta=True)
    


class SubjectTeaching(models.Model):
    '''
    a teacher can choose to say that they teach which subject at which grade
    This will allow us to tune content for them
    '''
    teacher  =  models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = grade = models.IntegerField()
    