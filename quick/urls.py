from django.urls import path

from . import views, lessons, chatbot, users

urlpatterns = [
    # chatbot endpoints
    path('chatbot/lesson/<id>/detail', chatbot.detail),

    # lessons
    path('hello', views.hello_world),
    path('hello/<name>/', views.hello_name),
    path('lessons/trending', lessons.trending),
    path('lessons/recommended', lessons.recommended),
    path('lessons/<id>/comments', lessons.comments),
    path('lessons/<id>/detail', lessons.detail),
    path('lessons/<id>/files', lessons.files),
    
    #users
    path('users/<id>/recent', users.recent),
]
