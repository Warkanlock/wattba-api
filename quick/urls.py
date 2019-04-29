from django.urls import path

from . import views, lessons, chatbot

urlpatterns = [
    # chatbot endpoints
    path('chatbot/lesson/<id>/detail', chatbot.detail),

    # users
    path('hello', views.hello_world),
    path('hello/<name>/', views.hello_name),
    path('lessons/trending', lessons.trending),
    path('lessons/recommended', lessons.recommended),
    path('lessons/<id>/comments', lessons.comments),
    path('lessons/<id>/detail', lessons.detail),
    #path('lessons/<id>/files')
]
