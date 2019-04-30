# wattba-api
============

## Getting started

### Create a virtualenv and activate it:

```
$ pip install -r requirements.txt``
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
```

to access the backend API: `localhost:8000/api/v1/backend/`


### Run elastic search:

```
./elasticsearch-5.1.1/bin/elasticsearch
```

In a new tab:
```
$ manage.py shell
$ from api.search import *
$ bulk_indexing()
```

Go to: 

`http://127.0.0.1:9200/lessoncontent-index/lesson_content_index/1/`

## Mock Endpoints

### Chatbot Endpoints

`/api/quick/chatbot/lessons/<id>/detail`

`id` required

**returns:**
```json
{
    "title": "Maths Lesson A",
    "content": "When you learn maths, you will be able to count... well sorta",
    "summary": "Some summary about a math lesson",
    "grade": 1
}
```

`/api/quick/chatbot/lessons?subject_id=<id>`

`id` is optional

**returns:**
```json
[{
    "title": "English Lesson b",
    "content": "This is a relevant lesson... tis is",
    "summary": "English is better than Spanish Nano!",
    "grade": 2,
    "subject": "Science"
}]
```

### Lessons Endpoints

`/api/quick/lessons/trending`

**returns:**
```json
[{
    "id": 3,
    "tags": "Math,Physics,IT",
    "title": "Cool lesson title 1",
    "description": "..."
}]
```

`/api/quick/lessons/recommended`

**returns:**
```json
[{
    "id": 0,
    "tags": "Math,Physics,IT",
    "title": "Dummy title 1",
    "description": "..."
}]
```