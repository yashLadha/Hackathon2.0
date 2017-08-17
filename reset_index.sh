#!/usr/bin/env bash

curl -XDELETE 'localhost:9200/_all'

echo ''

curl -XPUT 'localhost:9200/django?pretty' -H 'Content-Type: application/json' -d'
{
    "settings" : {
        "index" : {
            "number_of_shards" : 5,
            "number_of_replicas" : 1
        }
    }
}
'

