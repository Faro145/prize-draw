from flask import url_for
from flask_testing import TestCase

from numbers import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestNumbers(TestBase):

def test_numbers(self):
    number_one = "1"
    number_two = "9"
    number_three = "0"
    response = self.client.get(url_for('numbers'))
    self.assertIn(response.data, numbers)