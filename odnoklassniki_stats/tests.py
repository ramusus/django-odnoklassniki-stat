from django.test import TestCase
from django.test import Client
import unittest
from views import call
from odnoklassniki_groups.models import Group
from odnoklassniki_api.models import OdnoklassnikiContentError

class GetInfoTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_details(self):

        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual({'uid': '53071116239053'})
