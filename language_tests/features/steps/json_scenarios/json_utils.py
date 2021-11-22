import requests
import json
import unittest

def get_url():
    return 'https://test.jasgme.com/sgme/api'

def get_valid_credentials():
    return {'login': 'test.sgme@gmail.com', 'password': 'abcd1234'}

def get_token():
    url = get_url()
    body = get_valid_credentials()
    response = requests.post(f'{url}/authenticate/login', json=body)
    assert response.status_code == 200

    json_data = json.loads(response.text)

    token = json_data['token']

    auth = f'Bearer {token}'

    return auth
