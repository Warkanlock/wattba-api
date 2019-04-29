from elasticsearch_dsl.connections import connections

from elasticsearch_dsl import DocType, Text, Date, Search, MultiSearch, Integer
from elasticsearch_dsl.query import MultiMatch

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class LessonContentIndex(DocType):
    content = Text()
    title = Text()
    tags = Text()
    summary = Text()
    key = Integer()

    class Meta:
        index = 'lessoncontent-index'

def bulk_indexing():

    LessonContentIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Lesson.objects.all().iterator()))

def search_content(search, arr=[]):
    
    search = Search().query('match', content=search).execute()
    # return objects
    for value in search.hits:
        if value not in arr:
            arr.append(value['id'])
    return arr

def search_tags(search, arr=[]):
    
    search = Search().query('match', tags=search).execute()
    # return objects
    for value in search.hits:
        if value not in arr:
            arr.append(value['id'])
    return arr

def search_title(search, arr=[]):
    
    search = Search().query('match', title=search).execute()
    # return objects
    for value in search.hits:
        if value not in arr:
            arr.append(value['id'])
    return arr

def search_summary(search, arr=[]):
    
    search = Search().query('match', summary=search).execute()
    # return objects
    for value in search.hits:
        if value not in arr:
            arr.append(value['id'])
    return arr
