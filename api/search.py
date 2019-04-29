from elasticsearch_dsl.connections import connections

from elasticsearch_dsl import DocType, Text, Date, Search, MultiSearch
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

    class Meta:
        index = 'lessoncontent-index'

def bulk_indexing():

    LessonContentIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Lesson.objects.all().iterator()))

def search_content(search):

    ms = MultiSearch(index='lessoncontent-index')
    ms = ms.add(Search().query('match', content=search))
    ms = ms.add(Search().query('match', summary=search))
    ms = ms.add(Search().query('match', tags=search))
    # return objects
    return ms.execute()


