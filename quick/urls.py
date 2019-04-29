from django.urls import path

from . import views

urlpatterns = [
	# users
	path('hello', views.hello_world),
	path('hello/<name>/', views.hello_name),
    path('lessons/trending', views.trending),
    path('lessons/recommended', views.recommended),
    #path('lessons/<id>/comments'),
    #path('lessons/<id>/detail'),
    #path('lessons/<id>/files')
]
