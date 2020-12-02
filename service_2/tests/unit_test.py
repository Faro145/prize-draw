from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestLetters(TestBase):
    
    def test_letters(self):
        response = self.client.get(url_for('get_letters'))
        self.assertEquals(response.status_code, 200)
