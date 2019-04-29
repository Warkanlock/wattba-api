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
