import unittest
from flask import url_for
from os import getenv
from unittest.mock import patch
from flask_testing import TestCase
from application import app,db
from application.models import Prize_Draw

class TestBase(TestCase):

    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('DB_URI'),
        SECRET_KEY=getenv('KEY'),
        WTF_CSRF_ENABLED=False,
        DEBUG=True
        )
        return app
    
    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        testPrize = Prize_Draw(
            id = 1,
            letters = "PFx",
            numbers = "436",
            prize = "You have not won a prize"
        )      

        db.session.add(testPrize)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_prizedraw(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = '436'
                p.return_value.text = 'You have not won a prize'
            response = self.client.get(url_for('prizedraw'))
            self.assertEqual(response.status_code, 200)

