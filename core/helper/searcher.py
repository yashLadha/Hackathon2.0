from elasticsearch import Elasticsearch


def get_search():
    es = Elasticsearch()
    return es
