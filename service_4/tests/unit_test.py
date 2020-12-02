from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_big_prize(self):
        with patch('requests.get') as g:
            g.return_value.text = '371'
            response = self.client.post(
                url_for('get_prize'),
                data="371",
                follow_redirects=True)
            self.assertIn(b'You won a big prize', response.data)
    
    def test_no_prize(self): 
        response = self.client.post(
            url_for('get_prize'),
            data="563",
            follow_redirects=True
        )
        self.assertIn(b'You have not won a prize', response.data)



