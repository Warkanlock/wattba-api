# wattba-api
============

Getting started
~~~~~~~~~~~~~~~~
Create a virtualenv and activate it

  `` pip install -r requirements.txt``
  `` ./manage.py migrate``
  `` ./manage.py createsuperuser``
  `` ./manage.py runserver``

  to access the backend api `localhost:8000/api/v1/backend/`

Run elastic search:
~~~~~~~~~~~~~~~~~~~~~
`` ./elasticsearch-5.1.1/bin/elasticsearch ``
In a new tab
`` manage.py shell ``
``from api.search import *``
``bulk_indexing()``
go to ``http://127.0.0.1:9200/lessoncontent-index/lesson_content_index/1/``



# Endpoints

## /quick

``/api/quick/chatbot/lesson/<id>/detail``

`id` required

returns:
```json
{
    "title": "Maths Lesson A",
    "content": "When you learn maths, you will be able to count... well sorta",
    "summary": "Some summary about a math lesson",
    "grade": 1
}
```

``/api/quick/lessons/recommended``

returns:
```json
    [{
        'id': 0,
        'tags': 'Math,Physics,IT',
        'title': 'Dummy title 1',
        'description': '...'
    },
    {
        'id': 1,
        'tags': 'Math,Physics',
        'title': 'Dummy title 2',
        'description': '...'
    },
    {
        'id': 2,
        'tags': 'Math,Physics',
        'title': 'Dummy title 3',
        'description': '...'
    }]
```