from django.http import JsonResponse

from api.models import Lesson


def recommended(request):

    count = 0
    lessons = Lesson.objects.all()
    results = []

    for l in lessons:
        count += 1
        if count < 3:
            results.append({
                'id': l.id,
                'tags': l.tags,
                'title': l.title,
                "bookmarked": l.bookmarked,
                'description': l.content
            })

    return JsonResponse(results, safe=False)


def trending(request):
    count = 0
    lessons = Lesson.objects.all()
    results = []

    for l in lessons:
        count += 1
        if count < 3:
            results.append({
                'id': l.id,
                'tags': l.tags,
                'title': l.title,
                "bookmarked": l.bookmarked,
                'description': l.content
            })

    return JsonResponse(results, safe=False)


def comments(request, id):
    data = [
        {
            'id': 0,
            'user_id': 0,
            'user_logo': 'https://randomuser.me/api/portraits/women/36.jpg',
            'date': '2019-04-28T18:46:16+00:00',
            'stars': 4,
            'review': 'Sweet roll cupcake muffin oat cake bonbon marshmallow. Gingerbread wafer oat cake. Lemon drops pie donut pie gummies fruitcake marshmallow. Tiramisu chocolate cake carrot cake jelly beans jelly beans. Halvah halvah apple pie donut. Bonbon gingerbread fruitcake jelly cake candy canes lollipop.',
        },
        {
            'id': 1,
            'user_id': 1,
            'user_logo': 'https://randomuser.me/api/portraits/women/4.jpg',
            'date': '2019-04-27T18:46:16+00:00',
            'stars': 3,
            'review': 'Soufflé chocolate cake cheesecake candy canes wafer. Biscuit pudding jelly beans sugar plum donut. Chupa chups halvah sweet roll danish apple pie pudding chupa chups. Marshmallow gingerbread dessert. Marzipan jelly chocolate chocolate cake halvah dragée pie cake. Sweet jelly-o dessert biscuit chocolate liquorice ice cream danish danish. Dessert ice cream marshmallow cake muffin chocolate cake toffee sweet soufflé.',
        },
        {
            'id': 2,
            'user_id': 2,
            'user_logo': 'https://randomuser.me/api/portraits/men/9.jpg',
            'date': '2019-04-26T18:46:16+00:00',
            'stars': 5,
            'review': 'Carrot cake toffee pudding. Croissant cheesecake jelly. Topping danish chocolate bar sweet.',
        }
    ]

    return JsonResponse(data, safe=False)


def detail(request, id):
    lesson = Lesson.objects.get(pk=id)

    data = [
        {
            'age_range': lesson.age_range,
            'title': lesson.title,
            'translation': lesson.translation,
            'subject_matter': lesson.subject_matter,
            'topic': lesson.topic,
            'activity_type': lesson.activity_type,
            'duration': lesson.duration,
            'description': lesson.content,
            'rating': lesson.rating,
            'votes': lesson.votes,
            'supplies': lesson.supplies,
             "image": "https://via.placeholder.com/2000x2000.png?text={}".format(lesson.title)
        }
    ]

    return JsonResponse(data, safe=False)


def bookmark(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    lesson.bookmarked ^= True
    lesson.save()

    data = {
        "bookmarked": lesson.bookmarked
    }

    return JsonResponse(data, safe=False)

def files(request, id):
    data = [
        {
            'id': 0,
            'type': 'doc',
            'name': 'curriculum.docx',
        }, {
            'id': 1,
            'type': 'pdf',
            'name': 'curriculum.pdf',
        },
        {
            'id': 2,
            'type': 'jpg',
            'name': 'planets.jpg',
        }
    ]

    return JsonResponse(data, safe=False)
