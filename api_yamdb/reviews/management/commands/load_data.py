from django.core.management.base import BaseCommand
from django.conf import settings
from reviews.models import Category, Comment, Genre, Review, Title, User
import csv


CSV_DATA = {
    'category.csv': Category,
    'comments.csv': Comment,
    'genre.csv': Genre,
    'review.csv': Review,
    'titles.csv': Title,
    'users.csv': User,
}


class Command(BaseCommand):
    help = 'Load CSV files'

    def handle(self, *args, **kwargs):
        for csv_load_file, model in CSV_DATA.items():
            try:
                with open(
                    f'{settings.BASE_DIR}/static/data/{csv_load_file}',
                    'r',
                    encoding='utf-8'
                ) as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    model.objects.bulk_create(
                        model(**data) for data in csv_reader
                    )
                self.stdout.write(self.style.SUCCESS(f'Файл "{csv_load_file}" загружен!'))
            except ValueError as error:
                print(f'Ошибка при загрузке файла "{csv_load_file}"! {error}')
