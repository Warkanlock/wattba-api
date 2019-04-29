from django.urls import path

from . import views

urlpatterns = [
	# users
	path('', views.LessonsList.as_view()),
	path('user/<slug:pk>/', views.UserDetail.as_view()),
	path('users/', views.UserList.as_view()),
	path('new_users/', views.UserCreate.as_view()),

	# subjects
	
	# lessons

]
