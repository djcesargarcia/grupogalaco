from django.test import TestCase
from routes.models import Routes

# Create your tests here.

class RoutesTest(TestCase):
    def setUp(self):
        route_a = Routes(place="Las Palmas", origin="Mesa y Lopez", destiny="San Mateo", postal_code="35016")
        route_a.save() 
        
        