from django.http import JsonResponse

from api.models import Lesson


def recent(request, id):
    count = 0
    lessons = Lesson.objects.all()
    results = []

    for l in lessons:
        count += 1
        if count <= 5:
            results.append({
                'id': l.id,
                'tags': l.tags,
                'title': l.title,
                'description': l.summary
            })

    return JsonResponse(results, safe=False)


def bookmarked(request):
    count = 0
    lessons = Lesson.objects.filter(bookmarked=True)
    results = []

    for l in lessons:
        count += 1
        if count <= 3:
            results.append({
                'id': l.id,
                'tags': l.tags,
                'title': l.title,
                'description': l.summary
            })

    return JsonResponse(results, safe=False)