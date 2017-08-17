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


def get_id_by_pincode(pincode):
    pass
