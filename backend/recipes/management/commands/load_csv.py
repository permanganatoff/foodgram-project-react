import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    """Loading ingredients.csv to database."""

    def handle(self, *args, **kwargs):
        print('Loading ingredients.csv')
        file_path = './data/ingredients.csv'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                Ingredient.objects.update_or_create(
                    name=row[0],
                    measurement_unit=row[1])
        print('Data uploaded')
