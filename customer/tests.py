from django.test import TestCase
from customer.models import Customer

class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/routes/edit.html')
        self.assertEqual(response.status_code, 200)
        
    def test_index(self):
        response = self.client.get('/routes/index.html')
        self.assertEqual(response.status_code, 200)
        
    def setUp(self):
        mycustomer = Customer.objects.create(place= 'El Sobradillo')
    
    def test_customer_name(self):
        """Customer name is correctly"""
        customer_name = Customer.objects.get(name="lion")
       