from flask import url_for
from flask_testing import TestCase

from letters import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestLetters(TestBase):

def test_letters(self):
    letter_one = "A"
    letter_two = "k"
    letter_three = "G"
    response = self.client.get(url_for('letters'))
    self.assertIn(response.data, letters)