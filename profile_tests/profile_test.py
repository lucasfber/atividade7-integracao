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


class Profile(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_profiles(self):
        auth = get_token()

        header = {'authorization': auth}
        response = requests.get(f'{self.url}/profiles', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        for profile in json_data:
            self.assertIn('id', profile)
            self.assertEqual(type(profile['id']), int)


        for profile in json_data:
            self.assertIn('name', profile)
            self.assertEqual(type(profile['name']), str)

        for profile in json_data:
            self.assertIn('type', profile)
            self.assertEqual(type(profile['type']), str)