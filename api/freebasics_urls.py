from django.urls import path
import django.contrib.auth.urls
from . import freebasics_views

from django.conf.urls import url
from django.urls import include


urlpatterns = [
	# users
	path('', freebasics_views.HomeView.as_view(), name='home'),
	path('auth/', include(django.contrib.auth.urls)),
	path('lessons/<slug:pk>/', freebasics_views.LessonDetailView.as_view(), name='lesson-detail'),
	path('lessons/', freebasics_views.LessonListView.as_view(), name='lesson-list'),
	path('lessons/<slug:pk>/', freebasics_views.LessonDetailView.as_view(), name='lesson-detail'),
	path('subjects/<slug:pk>/', freebasics_views.SubjectDetailView.as_view(), name='subject-detail'),
]
