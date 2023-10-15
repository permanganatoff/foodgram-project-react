import csv

from django.core.management.base import BaseCommand

from backend.settings import CSV_DATA_DIR

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Uploading data about ingredients to the database'

    def handle(self, *args, **kwargs):

        with open(
            f'{CSV_DATA_DIR}', 'r', encoding='utf8'
        ) as file_csv:
            reader = csv.reader(file_csv, delimiter=',')
            Ingredient.objects.bulk_create(
                Ingredient(
                    name=row[0],
                    measure_unit=row[1],
                )
                for row in list(reader)[1:]
            )
        self.stdout.write(
            f'Файл импортирован в БД {Ingredient}'
        )

    print('Data uploaded to the database')
