from django.urls import path

from . import views

urlpatterns = [
	# users
	path('hello', views.hello_world),
	path('hello/<name>/', views.hello_name),
]
