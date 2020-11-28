from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_prize_on_page(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "Bzk371"
                p.return_value.text = "You won a big prize"

            response = self.client.get(url_for('index'))
            self.assertIn(b'Entry code: Bzk371 Result: You won a big prize', response.data)
