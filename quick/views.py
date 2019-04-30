from django.http import JsonResponse


def hello_world(request):
    # example using query parameters
    hallo = request.GET.get('name')

    data = {
        'hello': 'world',
    }

    if hallo is not None:
        data = {
            'hello': hallo,
        }

    return JsonResponse(data)


# example using url parameters
def hello_name(request, name):
    data = {
        'hello': name,
    }

    return JsonResponse(data)

