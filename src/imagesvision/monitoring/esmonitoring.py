from elasticsearch import Elasticsearch


def send_to_es(json,es):
    es.index(index='visionpython',doc_type='_doc',body=json)

def initiate_es():
    es = Elasticsearch()
    return es

