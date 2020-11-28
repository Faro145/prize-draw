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

def test_big_prize(self):
    response = self.client.post(
            url_for('prize_code'),
            data="Bzk371",
            follow_redirects=True
        )
    self.assertIn(b'You won a big prize', response.data)



