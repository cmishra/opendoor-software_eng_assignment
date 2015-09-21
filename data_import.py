import pandas as pd, os, django, sys

# os.environ.setdefault('DJANGO_SETTING_MODULE', 'gettingstarted.settings')
# django.setup()
# from django.conf import settings
# from gettingstarted import myapp_
# settings.configure(DEBUG=True)
sys.path.append('C:\Users\Chetan\Dropbox\College\4_Fourth Year\Job Stuff\Opendoor project\SoftwareDev')
os.environ['DJANGO_SETTINGS_MODULE'] = 'gettingstarted.settings'
from listings.models import House


data = pd.read_csv(open('data/listings.csv'))
for index, row in data.iterrows():
    house = House(id=int(float(row['id'])),
                  price=row['price'],
                  street=row['street'],
                  bedrooms=row['bedrooms'],
                  bathrooms=row['bathrooms'],
                  sq_ft=row['sq_ft'])
    house.save()
