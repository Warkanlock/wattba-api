import requests
from django.http import JsonResponse
from api.models import Lesson
from django.utils.html import strip_tags


def translate(request, lesson_id, dst):
    input = 'Cupcake ipsum dolor sit amet danish wafer. Marshmallow danish carrot cake chocolate chocolate bar cake. Gummi bears caramels halvah toffee. Oat cake caramels dessert bear claw biscuit. Candy tootsie roll lemon drops jelly beans donut sweet roll chupa chups tiramisu jujubes. Muffin chocolate cake cake carrot cake powder pastry. Toffee halvah cake jelly carrot cake. Danish powder candy biscuit jelly.'

    result = translate_api(input, dst)

    data = {
        'action': 'translated',
        'result': result,
    }

    return JsonResponse(data, safe=False)


def translate_detail(request, lesson_id, dst):
    lesson = Lesson.objects.get(pk=lesson_id)

    data = [
        {
            'age_range': lesson.age_range,
            'title': translate_eng_api(lesson.title, dst),
            'translation': lesson.translation,
            'subject_matter': translate_eng_api(lesson.subject_matter, dst),
            'topic': lesson.topic,
            'activity_type': lesson.activity_type,
            'duration': lesson.duration,
            'description': translate_eng_api(lesson.content, dst),
            'rating': lesson.rating,
            'votes': lesson.votes,
            'supplies': lesson.supplies,
             "image": "https://via.placeholder.com/2000x2000.png?text={}".format(lesson.title)
        }
    ]

    return JsonResponse(data, safe=False)


def translate_eng_api(text, dst):
    return translate_api(text, 'en', dst)


def translate_api(text, src, dst):
    post_data = {
        "text": text,
        "src_lang": src,
        "dst_lang": dst
    }

    result = requests.post(
        'http://18.236.191.192:3000/translate',
        json=post_data,
    )

    return result.json()['result']


def summary(request, lesson_id):
    input = 'Cupcake ipsum dolor sit amet danish wafer. Marshmallow danish carrot cake chocolate chocolate bar cake. Gummi bears caramels halvah toffee. Oat cake caramels dessert bear claw biscuit. Candy tootsie roll lemon drops jelly beans donut sweet roll chupa chups tiramisu jujubes. Muffin chocolate cake cake carrot cake powder pastry. Toffee halvah cake jelly carrot cake. Danish powder candy biscuit jelly.'

    # a sequence of two element tuples
    post_data = {
        "text": input
    }

    result = requests.post(
        'http://18.236.191.192:3000/summary',
        json=post_data,
    )

    result = result.json()['result']

    data = {
        'action': 'summarized',
        'result': result,
    }

    return JsonResponse(data, safe=False)
