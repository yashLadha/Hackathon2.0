from datetime import datetime

from elasticsearch import NotFoundError

from core.models import User


def preprocess_date(date_):
    """Preprocess date string to use in datefiled in database
    :param date_ : date string
    :return formatted datetime object
    """
    if 'JAN' in date_:
        date_ = date_.replace('JAN', '01')
    elif 'FEB' in date_:
        date_ = date_.replace('FEB', '02')
    elif 'MAR' in date_:
        date_ = date_.replace('MAR', '03')
    elif 'APR' in date_:
        date_ = date_.replace('APR', '04')
    elif 'MAY' in date_:
        date_ = date_.replace('MAY', '05')
    elif 'JUN' in date_:
        date_ = date_.replace('JUN', '06')
    elif 'JUL' in date_:
        date_ = date_.replace('JUL', '07')
    elif 'AUG' in date_:
        date_ = date_.replace('AUG', '08')
    elif 'SEP' in date_:
        date_ = date_.replace('SEP', '09')
    elif 'OCT' in date_:
        date_ = date_.replace('OCT', '10')
    elif 'NON' in date_:
        date_ = date_.replace('NON', '11')
    elif 'DEC' in date_:
        date_ = date_.replace('DEC', '12')
    if date_[-2:] > '17':
        date_ = date_[:6] + '19' + date_[-2:]
    else:
        date_ = date_[:6] + '20' + date_[-2:]
    return datetime.strptime(date_, '%d-%m-%Y')


def family_detail_extractor(data):
    """Extracts the family details of one family
    :param data : Json data for extraction
    :return family_list : Returns the json list user objects
    """
    family_list = {}
    try:
        cnt = 0
        family_id = data['hof_Details']['FAMILYIDNO']
        for key in data:
            if key == 'family_Details':
                for items in data[key]:
                    cnt = user_entry(cnt, family_list, items, False, family_id)
            elif key == 'hof_Details':
                cnt = user_entry(cnt, family_list, data[key], True, family_id)
        return family_list
    except AttributeError:
        print 'Json object cannot be decoded // Extractor'


def user_entry(cnt, family_list, items, hof, family_id):
    user = User()
    user_json = {}
    try:
        obj = User.es.search(items['AADHAR_ID'])
        if not obj:
            push_user(cnt, family_list, items, user, user_json, hof, family_id)
        cnt += 1
    except NotFoundError:
        print 'Index is not created'
    return cnt


def push_user(cnt, family_list, items, user, user_json, hof, family_id):
    """Commits the fetched user into the database"""
    for item_key in items:
        if item_key == 'AADHAR_ID':
            user.aadhaar_id = items[item_key]
            user_json['AADHAR_ID'] = items[item_key]
        elif item_key == 'NAME_ENG':
            user.name_eng = items[item_key]
            user_json['NAME_ENG'] = items[item_key]
        elif item_key == 'NAME_HND':
            user.name_hnd = items[item_key]
            user_json['NAME_HND'] = items[item_key]
        elif item_key == 'M_ID':
            user.m_id = items[item_key]
            user_json['M_ID'] = items[item_key]
        elif item_key == 'GENDER':
            user.gender = items[item_key]
            user_json['GENDER'] = items[item_key]
        elif item_key == 'DOB':
            date_ = preprocess_date(items[item_key])
            user.dob = date_
            user_json['DOB'] = str(date_)
    if hof:
        user.hof = True
        user_json['HOF'] = True
    else:
        user_json['HOF'] = user.hof
    user.family_id = family_id
    user_json['FAMILY_ID'] = family_id
    user.save()
    family_list[cnt] = user_json
