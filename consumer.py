import requests

provider_api_path = 'http://localhost:8000'


def get_user(user_id, api_baseurl):
    """Fetch a user object by user_name from the server."""
    uri = api_baseurl + '/users/' + str(user_id)
    return requests.get(uri, auth=('admin', 'Password123')).json()
