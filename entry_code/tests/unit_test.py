from flask import url_for
from flask_testing import TestCase

from entry_code import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestEntryCode(TestBase):

def test_entry_code(self):
        letters = "BpT"
        numbers = "538"
        response = self.client.get(url_for('entry_code'))
        self.assertIn(response.data, entry_code)



