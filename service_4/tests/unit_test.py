from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_entry_code(self):
        letters = "BpT"
        numbers = "538"
        response = self.client.get(url_for('get_entry_code'))
        self.assertIn(response.data, entry_code)
    
    def test_big_prize(self):
        response = self.client.post(
            url_for('get_entry_code'),
            data="Bzk371",
            follow_redirects=True
        )
        self.assertIn(b'You won a big prize', response.data)
    
    def  response = self.client.post(
            url_for('get_entry_code'),
            data="Bzk371",
            follow_redirects=True
        )
        self.assertIn(b'You have not won a prize', response.data)



