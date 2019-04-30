from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models


class LessonDetailView(DetailView):

    model = models.Lesson


class HomeView(ListView):

    model = models.Lesson


class LessonListView(ListView):

    model = models.Lesson
