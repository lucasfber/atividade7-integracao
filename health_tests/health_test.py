import unittest
import requests
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, 'features/steps/json_scenarios')
sys.path.append(path_dir)

from json_utils import  *


class Health(unittest.TestCase):
    def setUp(self):
        self.url = get_url()


    def test_1_get_health(self):
        response = requests.get(f"{self.url}/health")
        assert response.status_code == 200
        self.assertEqual('Healthy', response.text)
