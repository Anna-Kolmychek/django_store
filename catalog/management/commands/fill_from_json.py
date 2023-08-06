import json

from django.core.management import BaseCommand

from catalog.models import Category, Product

FIXTURE_FILE = 'data.json'


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open(FIXTURE_FILE, 'r', encoding='utf-8') as file:
            file_data = json.load(file)

        categories_list = []
        products_list = []
        for item in file_data:
            if 'category' in item['model']:
                categories_list.append(Category(
                    pk=item['pk'],
                    name=item['fields']['name'],
                    description=item['fields']['description']
                ))
        for item in file_data:
            if 'product' in item['model']:

                category = None
                for category_item in categories_list:
                    if category_item.pk == item['fields']['category']:
                        category = category_item
                        break

                products_list.append(Product(
                    pk=item['pk'],
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    image=item['fields']['image'],
                    category=category,
                    price=item['fields']['price'],
                    created_at=item['fields']['created_at'],
                    changed_at=item['fields']['changed_at'],
                ))

        Category.objects.bulk_create(categories_list)
        Product.objects.bulk_create(products_list)
