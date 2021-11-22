import json
import unittest
import requests
import os
import sys
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, 'features/steps/json_scenarios')
sys.path.append(path_dir)

from json_utils import  *


class Authenticate(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_post_authenticate(self):
        body = get_valid_credentials()
        response = requests.post(f'{self.url}/authenticate/login', json=body)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        self.assertIn('id', json_data)
        self.assertEqual(type(json_data['id']), int)

        self.assertIn('name', json_data)
        self.assertEqual(type(json_data['name']), str)

        self.assertIn('email', json_data)
        self.assertEqual(type(json_data['email']), str)

        self.assertIn('profile', json_data)
        self.assertEqual(type(json_data['profile']), dict)

        profile = json_data['profile']

        self.assertIn('id', json_data['profile'])
        self.assertEqual(type(profile['id']), int)

        self.assertIn('name', json_data['profile'])
        self.assertEqual(type(profile['name']), str)

        self.assertIn('type', json_data['profile'])
        self.assertEqual(type(profile['type']), str)


        for permission in json_data['permissions']:
            self.assertIn('tag', permission)
            self.assertEqual(type(permission['tag']), str)