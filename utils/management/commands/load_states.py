import pandas as pd
from django.core.management.base import BaseCommand
from utils.models import State


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        check_states = State.objects.all()
        if check_states:
            return "States already loaded."

        file_path = 'utils/data/pak_cities_states.csv'

        states_data_read = pd.read_csv(file_path)
        states_data_frame = pd.DataFrame(states_data_read, columns=['admin_name'])
        states_data_frame = states_data_frame.drop_duplicates()

        states_objects = []
        for state in states_data_frame['admin_name']:
            states_objects += [State(name=state)]
        states = State.objects.bulk_create(states_objects)
        