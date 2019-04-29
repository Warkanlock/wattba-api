from django.http import JsonResponse

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

def trending(request):
    data = [{
        'id': 3,
        'tags': 'Math,Physics,IT',
        'title': 'Cool lesson title 1',
        'description': 'Lollipop gingerbread sweet roll. Marshmallow macaroon bonbon tart cupcake. Ice cream candy canes candy canes dessert bonbon muffin ice cream. Pastry cotton candy sweet roll. Chocolate soufflé chocolate cake tiramisu biscuit oat cake bear claw brownie. Candy sweet apple pie sweet sweet icing dessert candy canes.'
    },
    {
        'id': 4,
        'tags': 'Math,IT',
        'title': 'Cool lesson title 2',
        'description': 'Lollipop gingerbread sweet roll. Marshmallow macaroon bonbon tart cupcake. Ice cream candy canes candy canes dessert bonbon muffin ice cream. Pastry cotton candy sweet roll. Chocolate soufflé chocolate cake tiramisu biscuit oat cake bear claw brownie. Candy sweet apple pie sweet sweet icing dessert candy canes.'
    },
    {
        'id': 5,
        'tags': 'IT,Science',
        'title': 'Cool lesson title 3',
        'description': 'Lollipop gingerbread sweet roll. Marshmallow macaroon bonbon tart cupcake. Ice cream candy canes candy canes dessert bonbon muffin ice cream. Pastry cotton candy sweet roll. Chocolate soufflé chocolate cake tiramisu biscuit oat cake bear claw brownie. Candy sweet apple pie sweet sweet icing dessert candy canes.'
    }]

    return JsonResponse(data, safe=False)

def comments(request, id):
    data = [{
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
    }]

    return JsonResponse(data, safe=False)

def detail(request, id):
    data = [{
        'age_range': '11-13',
        'language': 'English',
        'translation': 'Available',
        'subject_matter': 'Science',
        'topic': 'Planets',
        'activity_type': 'Project',
        'duration': '3 days',
        'description': 'Cookie donut cotton candy. Chupa chups wafer icing gummies pudding cake jelly-o. Cake cupcake cotton candy bonbon marzipan topping chocolate cake. Jelly-o cookie halvah apple pie donut bear claw liquorice apple pie gummies. Cheesecake dragée chocolate cake pudding. Sugar plum jelly beans pie halvah apple pie. Chupa chups dragée cake.',
        'rating': 4,
    }]

    return JsonResponse(data, safe=False)

def files(request, id):
    data = [{
        'id': 0,
        'type': 'doc',
        'name': 'curriculum.docx',
    },{
        'id': 1,
        'type': 'pdf',
        'name': 'curriculum.pdf',
    },{
        'id': 2,
        'type': 'jpg',
        'name': 'planets.jpg',
    }]

    return JsonResponse(data, safe=False)
