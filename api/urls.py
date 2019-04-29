from django.urls import path

from . import views

urlpatterns = [
	# users
	path('', views.HomeView.as_view()),
	path('user/<slug:pk>/', views.UserDetail.as_view()),
	path('users/', views.UserList.as_view()),
	path('new_users/', views.UserCreate.as_view()),

	# subjects
	path('subjects/', views.SubjectsList.as_view()),
	path('subjects/<slug:pk>/', views.SubjectDetail.as_view()),

	# lessons
	path('lessons/', views.LessonsList.as_view()),
	path('lessons/<slug:pk>/', views.LessonDetail.as_view()),
]
