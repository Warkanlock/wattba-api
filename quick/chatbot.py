import json

from django.http import JsonResponse, HttpResponseServerError, HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    grade = request.GET.get('grade')

    if subject_id is not None:
        lessons = Lesson.objects.filter(subject__id=subject_id)
    else:
        lessons = Lesson.objects.all()

    data = []

    for l in lessons:
        if (grade is not None and int(grade) == l.grade) or (grade is None):
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


@csrf_exempt
def create(request):
    data = {
        'info': 'Not working',
    }

    if request.method == 'POST':
        json_data = json.loads(request.body)  # request.raw_post_data w/ Django < 1.4
        try:
            link = json_data['link']

            if link is not None:
                data = {
                    'info': 'Great Success',
                    'received': link
                }
        except KeyError:
            HttpResponseServerError("Malformed data!")
        HttpResponse("Got json data")

    return JsonResponse(data, safe=False)