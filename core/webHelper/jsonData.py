import requests as req


def get_json_data(url):
    """Get json data from the specified url
    :param url : Api request url
    """
    req_res = req.get(url)
    try:
        json_data = req_res.json()
        return json_data
    except ValueError:
        print 'Json cannot be decoded'
        return None
