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


class Language(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_languages(self):
        auth = get_token()

        header = {'authorization': auth}
        response = requests.get(f'{self.url}/languages', headers=header)
        assert response.status_code == 200