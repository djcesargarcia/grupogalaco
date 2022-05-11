from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from country.models import Country


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
Uploading our data to Mysql Database
"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from countries.csv"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Country.objects.exists():
            print('child data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading countries data")


        #Code to load the data into database
        for row in DictReader(open('./countries.csv')):
            child=Country(continent=row['Continent'], country=row['Country'])  
            child.save()