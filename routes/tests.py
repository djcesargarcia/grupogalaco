from django.test import TestCase
from routes.models import Routes

# Create your tests here.

class RouteTest(TestCase):
    def setUp(self):
        route_a = Routes(place="La Gomera", origin="Valle Gran Rey", destiny="San Sebastian de la Gomera", postal_code="35016")
        route_a.save() 
        
        
        
        