from core.helper import searcher
from core.models import User


def get_users_by_name(name_):
    """Returns the list of person whose username
    matches with that name
    """
    users = User.es.search(name_)
    return users


def get_family_by_aadhar(aadhar_no):
    """Get the family members by aadhar id
    and also the head of the family from that
    """
    users_list = User.es.search(aadhar_no)
    user_list = []
    for user in users_list:
        user_family_no = user['family_id']
        user_list = User.es.search(user_family_no)
    return user_list


def get_family_by_id(family_id_):
    """Get the details of family by family id"""
    family = User.es.search(family_id_)
    return family


def get_user_by_dbid(dbid):
    es = searcher.get_search()
    res = es.search(index='django', body={
        'query': {
            'match': {
                'id': dbid
            }
        }
    })
    return res['hits']['hits'][0]


def get_bhamashah_id(userId):
    es = searcher.get_search()
    res = es.search(index='bhamashah', body={
        'query': {
            'match': {
                'user': userId
            }
        }
    })
    return res['hits']['hits'][0]


def get_ids_by_pincode(pincode):
    """Get hof details from pincode"""
    es = searcher.get_search()
    res = es.search(index='location', body={
        'query': {
            "match": {
                'pincode': pincode
            }
        }
    })
    return res
