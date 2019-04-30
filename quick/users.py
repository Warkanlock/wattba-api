from django.http import JsonResponse

from api.models import Lesson


def recent(request, id):
    data = [{
        'id': 0,
        'title': 'My awesome recent project 1',
    },
    {
        'id': 1,
        'title': 'My awesome recent project 2',
    },
    {
        'id': 2,
        'title': 'My awesome recent project 3',
    }]

    return JsonResponse(data, safe=False)


def bookmarked(request):
    count = 0
    lessons = Lesson.objects.filter(bookmarked=True)
    results = []

    for l in lessons:
        count += 1
        if count < 3:
            results.append({
                'id': l.id,
                'tags': l.tags,
                'title': l.title,
                'description': l.summary
            })

    return JsonResponse(results, safe=False)