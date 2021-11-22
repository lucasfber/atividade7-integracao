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


class Sponsor(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_sponsors(self):
        auth = get_token()

        header = {'authorization': auth}
        response = requests.get(f'{self.url}/sponsors', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        for sponsor in json_data:
            self.assertIn('id', sponsor)
            self.assertEqual(type(sponsor['id']), int)

        for sponsor in json_data:
            self.assertIn('name', sponsor)
            self.assertEqual(type(sponsor['name']), str)

        for sponsor in json_data:
            self.assertIn('cnpj', sponsor)
            self.assertEqual(type(sponsor['cnpj']), str)

        for sponsor in json_data:
            self.assertIn('phone', sponsor)
            self.assertEqual(type(sponsor['phone']), str)

        for sponsor in json_data:
            self.assertIn('email', sponsor)
            self.assertEqual(type(sponsor['email']), str)

        for sponsor in json_data:
            self.assertIn('contactPerson', sponsor)
            self.assertEqual(type(sponsor['contactPerson']), str)

        for sponsor in json_data:
            self.assertIn('deleted', sponsor)
            self.assertEqual(type(sponsor['deleted']), bool)

        for sponsor in json_data:
            self.assertIn('country', sponsor)
            self.assertEqual(type(sponsor['country']), dict)

        # COUNTRY
        for sponsor in json_data:
            self.assertIn('id', sponsor['country'])
            self.assertEqual(type(sponsor['country']['id']), int)

        for sponsor in json_data:
            self.assertIn('name', sponsor['country'])
            self.assertEqual(type(sponsor['country']['name']), str)

        for sponsor in json_data:
            self.assertIn('active', sponsor['country'])
            self.assertEqual(type(sponsor['country']['active']), bool)

        for sponsor in json_data:
            self.assertIn('min_salary', sponsor['country'])
            self.assertEqual(type(sponsor['country']['min_salary']), float)

        for sponsor in json_data:
            self.assertIn('max_salary', sponsor['country'])
            self.assertEqual(type(sponsor['country']['max_salary']), float)
        # END COUNTRY

        # STATE
        for sponsor in json_data:
            self.assertIn('state', sponsor)
            self.assertEqual(type(sponsor['state']), dict)

        for sponsor in json_data:
            self.assertIn('id', sponsor['state'])
            self.assertEqual(type(sponsor['state']['id']), int)

        for sponsor in json_data:
            self.assertIn('name', sponsor['state'])
            self.assertEqual(type(sponsor['state']['name']), str)

        for sponsor in json_data:
            self.assertIn('active', sponsor['state'])
            self.assertEqual(type(sponsor['state']['active']), bool)

        for sponsor in json_data:
            self.assertIn('country', sponsor['state'])
            self.assertEqual(type(sponsor['state']['country']), dict)
        # END STATE

        # for sponsor in json_data:
        #     self.assertIn('editions', sponsor)
        #     self.assertEqual(type(sponsor['editions']), list)

        # for sponsor in json_data:
        #     self.assertIn('description', sponsor)
        #     self.assertEqual(type(sponsor['description']), str)
        #
        # for sponsor in json_data:
        #     self.assertIn('logoPath', sponsor)
        #     self.assertEqual(type(sponsor['logoPath']), str)
