from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    
    def test_numbers(self):
        number_one = "1"
        number_two = "9"
        number_three = "0"
        response = self.client.get(url_for('get_numbers'))
        self.assertIn(response.data, numbers)
