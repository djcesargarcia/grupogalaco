from django.test import TestCase

class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/routes/edit.html')
        self.assertEqual(response.status_code, 200)
        
    def test_index(self):
        response = self.client.get('/routes/index.html')
        self.assertEqual(response.status_code, 200)