# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse

from core.helper import query_helpers as qh


def family_details(request, family_id):
    """Extracts the family details and other features"""
    results = qh.get_family_by_id(family_id)
    res = []
    for item in results:
        user = {
            'name_eng': item['name_eng'],
            'aadhaar_id': item['aadhaar_id'],
            'dob': item['dob'],
            'hof': item['hof'],
            'name_hnd': item['name_hnd'],
            'gender': item['gender']
        }
        res.append(user)
    return JsonResponse(json.loads(json.dumps(res)), safe=False)


def location_details(request, pincode):
    results = qh.get_ids_by_pincode(pincode)
    users_list = []
    cnt = 0
    for item in results['hits']['hits']:
        user_id = item['_source']['user']
        users_fetched = qh.get_user_by_dbid(user_id)
        bhamashah_id = qh.get_bhamashah_id(user_id)
        print users_fetched['_source']['name_eng']
        print bhamashah_id['_source']['bhamashah_id']

        user = {'user_name': users_fetched['_source']['name_eng'],
                'bhamashah_id': bhamashah_id['_source']['bhamashah_id']}
        users_list.append(user)
    print users_list
    return JsonResponse(json.loads(json.dumps(users_list)), safe=False)
