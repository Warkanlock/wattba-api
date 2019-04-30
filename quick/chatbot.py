from django.http import JsonResponse
from api.models import Lesson
from django.utils.html import strip_tags


def detail(request, id):
    lesson = Lesson.objects.get(pk=id)

    data = {
        "lesson_id": lesson.id,
        "subject_id": lesson.subject.id,
        "title": lesson.title,
        "content": strip_tags(lesson.content),
        "summary": lesson.summary,
        "grade": lesson.grade,
        "subject": lesson.subject.name,
        "image": "https://via.placeholder.com/1000x1000.png?text={}".format(lesson.title)
    }

    return JsonResponse(data, safe=False)


def lessons_by_subject(request):
    subject_id = request.GET.get('subject_id')

    if subject_id is not None:
        lessons = Lesson.objects.filter(subject__id=subject_id)
    else:
        lessons = Lesson.objects.all()

    data = []

    for l in lessons:
        lesson = {
            "lesson_id": l.id,
            "subject_id": l.subject.id,
            "title": l.title,
            "content": strip_tags(l.content),
            "summary": l.summary,
            "grade": l.grade,
            "subject": l.subject.name,
            "image": "https://via.placeholder.com/1000x1000.png?text={}".format(l.title)
        }

        data.append(lesson)

    return JsonResponse(data, safe=False)
