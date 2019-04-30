from django.urls import path

from . import views, lessons, chatbot, users, pytorch

urlpatterns = [
    # chatbot endpoints
    path('chatbot/lessons/<id>/detail', chatbot.detail),
    path('chatbot/lessons', chatbot.lessons_by_subject),

    # pytorch endpoints
    path('pytorch/<lesson_id>/<dst>/translate/summary', pytorch.translate),
    path('pytorch/<lesson_id>/<dst>/translate/detail', pytorch.translate_detail),
    path('pytorch/<lesson_id>/summary', pytorch.summary),

    # lessons
    path('hello', views.hello_world),
    path('hello/<name>/', views.hello_name),
    path('lessons/trending', lessons.trending),
    path('lessons/recommended', lessons.recommended),
    path('lessons/<id>/comments', lessons.comments),
    path('lessons/<id>/detail', lessons.detail),
    path('lessons/<lesson_id>/bookmark', lessons.bookmark),
    path('lessons/<id>/files', lessons.files),
    
    #users
    path('users/<id>/recent', users.recent),
    path('users/bookmarked', users.bookmarked),
]
