import unittest
import json
from app import app, url_database


class TestURLShortener(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_shorten_url(self):
        # Test the /shorten endpoint
        payload = {'long_url': 'https://www.example.com'}
        response = self.app.post('/shorten', json=payload)

        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertIn('short_url', data)

    def test_redirect_to_long_url(self):
        # Test the /<short_url> endpoint
        payload = {'long_url': 'https://www.example.com'}
        response = self.app.post('/shorten', json=payload)

        data = json.loads(response.data.decode('utf-8'))
        short_url = data['short_url']

        response = self.app.get(f'/{short_url}')

        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('long_url', data)
        self.assertEqual(data['long_url'], 'https://www.example.com')

    def test_invalid_short_url(self):
        # Test handling of invalid short URL
        response = self.app.get('/invalid_short_url')

        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 404)
        self.assertIn('error', data)

    def tearDown(self):
        # Clear the in-memory database after each test
        url_database.clear()


if __name__ == '__main__':
    unittest.main()
