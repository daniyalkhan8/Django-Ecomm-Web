import pandas as pd
from django.core.management.base import BaseCommand
from products.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        check_categories = Category.objects.all()
        if check_categories:
            return "Categories already loaded."
        
        file_path = 'products/data/categories.csv'
        categ_data_read = pd.read_csv(file_path)
        categ_data_frame = pd.DataFrame(categ_data_read, columns=['name'])
        categ_data_frame = categ_data_frame.drop_duplicates()

        categ_objects = []
        for category_name in categ_data_frame['name']:
            categ_objects += [Category(name=category_name)]
        categories = Category.objects.bulk_create(categ_objects)
