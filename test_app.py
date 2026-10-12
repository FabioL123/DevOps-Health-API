Original path: devops-health-api/tests/test_app.py
Note: this PDF displays the file's text. It is not a runnable replacement for the original .py, .sql, .yml, or configuration file.
import os
import unittest
from app.main import create_app
class HealthApiTests(unittest.TestCase):
 def setUp(self):
 self.client = create_app().test_client()
 def test_health(self):
 response = self.client.get('/health')
 self.assertEqual(response.status_code, 200)
 self.assertEqual(response.get_json(), {"status": "ok"})
 def test_version(self):
 response = self.client.get('/version')
 self.assertEqual(response.status_code, 200)
 self.assertEqual(response.get_json()["name"], "devops-health-api")
 self.assertIn("version", response.get_json())
 def test_index(self):
 response = self.client.get('/')
 self.assertEqual(response.status_code, 200)
 self.assertIn('/health', response.get_json()["endpoints"])
 def test_unknown_route(self):
 response = self.client.get('/does-not-exist')
 self.assertEqual(response.status_code, 404)
 self.assertEqual(response.get_json(), {"error": "not_found"})
if __name__ == '__main__':
 unittest.m
