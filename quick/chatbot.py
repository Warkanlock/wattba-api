from django.http import JsonResponse
from api.models import Lesson

def detail(request, id):
    lesson = Lesson.objects.get(pk=1)

    data = {
        "name": lesson.title,
        "pew": "no"
    }

    return JsonResponse(data, safe=False)