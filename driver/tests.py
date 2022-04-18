from django.test import TestCase
from driver.models import Driver

# models test
class DriverTest(TestCase):
    def setUp(self):
        driver_a = Driver(name="Cesar", nif="78549785B", adress="calle don zoilo 34")
        driver_a.save()
   
        
        