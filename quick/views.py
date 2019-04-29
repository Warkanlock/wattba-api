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

def recommended(request):
    data = [{
        'id': 0,
        'tags': 'Math,Physics,IT',
        'title': 'Dummy title 1',
        'description': 'Lollipop gingerbread sweet roll. Marshmallow macaroon bonbon tart cupcake. Ice cream candy canes candy canes dessert bonbon muffin ice cream. Pastry cotton candy sweet roll. Chocolate soufflé chocolate cake tiramisu biscuit oat cake bear claw brownie. Candy sweet apple pie sweet sweet icing dessert candy canes.'
    },
    {
        'id': 1,
        'tags': 'Math,Physics',
        'title': 'Dummy title 2',
        'description': 'Lollipop gingerbread sweet roll. Marshmallow macaroon bonbon tart cupcake. Ice cream candy canes candy canes dessert bonbon muffin ice cream. Pastry cotton candy sweet roll. Chocolate soufflé chocolate cake tiramisu biscuit oat cake bear claw brownie. Candy sweet apple pie sweet sweet icing dessert candy canes.'
    },
    {
        'id': 2,
        'tags': 'Math,Physics',
        'title': 'Dummy title 3',
        'description': 'Lollipop gingerbread sweet roll. Marshmallow macaroon bonbon tart cupcake. Ice cream candy canes candy canes dessert bonbon muffin ice cream. Pastry cotton candy sweet roll. Chocolate soufflé chocolate cake tiramisu biscuit oat cake bear claw brownie. Candy sweet apple pie sweet sweet icing dessert candy canes.'
    }]

    return JsonResponse(data, safe=False)
