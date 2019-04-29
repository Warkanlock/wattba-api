from django.http import JsonResponse
from api.models import Lesson
from django.utils.html import strip_tags


def detail(request, id):
    lesson = Lesson.objects.get(pk=id)

    data = {
        "title": lesson.title,
        "content": strip_tags(lesson.content),
        "summary": lesson.summary,
        "grade": lesson.grade
    }

    return JsonResponse(data, safe=False)
