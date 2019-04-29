from django.urls import path

from . import views, lessons

urlpatterns = [
    # users
    path('hello', views.hello_world),
    path('hello/<name>/', views.hello_name),
    path('lessons/trending', lessons.trending),
    path('lessons/recommended', lessons.recommended),
    path('lessons/<id>/comments', lessons.comments),
    #path('lessons/<id>/detail'),
    #path('lessons/<id>/files')
]
