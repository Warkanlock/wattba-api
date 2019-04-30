from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic

from . import models


class LessonDetailView(DetailView):

    model = models.Lesson

    def post(self, request, *args, **kwargs):


	    if user.is_authenticated:
	        if 'search' in request.POST:
	        	print(request.POST)



class HomeView(ListView):

    model = models.Lesson


class LessonListView(ListView):

    model = models.Lesson


class SubjectDetailView(DetailView):

    model = models.Subject