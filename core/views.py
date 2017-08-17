# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import HttpResponse

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
            return HttpResponse(json.dumps(family_list))
    return HttpResponse('No data fetched for family list')
