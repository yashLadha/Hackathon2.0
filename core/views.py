# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse

from core.helper import query_helpers as qh
from extractors import family_detail
from webHelper import jsonData


def family_details(request):
    """Extracts the family details and other features"""
    data = jsonData.get_json_data(
        'https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/family/'
        'details/1067-7PVQ-28383?client_id=ad7288a4-7764-436d-a727-783a977f1fe1'
    )
    if data is not None:
        family_list = family_detail.family_detail_extractor(data)
        if family_list is not None:
            print family_list
            return JsonResponse(json.loads(json.dumps(family_list)))
    return HttpResponse('No data fetched for family list')


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
