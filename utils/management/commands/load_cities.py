import pandas as pd
from django.core.management.base import BaseCommand
from utils.models import City, State


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        check_cities = City.objects.all()
        
        if check_cities:
            return "Cities already loaded."

        file_path = 'utils/data/pak_cities_states.csv'

        cities_data_read = pd.read_csv(file_path)
        cities_data_frame = pd.DataFrame(cities_data_read, columns=['city', 'admin_name'])
        cities_data_frame = cities_data_frame.drop_duplicates()

        cities_records = []
        for index, row in cities_data_frame.iterrows():
            state_id = State.objects.get(name=row['admin_name'])
            cities_records += [City(name=row['city'], state_id=state_id)]
        cities = City.objects.bulk_create(cities_records)
