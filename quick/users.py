from django.http import JsonResponse

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