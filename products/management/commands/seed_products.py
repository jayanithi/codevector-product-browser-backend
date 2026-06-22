from django.core.management.base import BaseCommand
from products.models import Product
from decimal import Decimal
from django.utils import timezone
import random


class Command(BaseCommand):
    help = "Generate 200000 products"

    def handle(self, *args, **kwargs):

        products_by_category = {
            "Electronics": [
                "iPhone 16",
                "Samsung Galaxy S25",
                "MacBook Pro",
                "Dell Inspiron",
                "Smart Watch",
                "Bluetooth Speaker",
                "Gaming Mouse",
                "Headphones"
            ],

            "Books": [
                "Python Programming",
                "Machine Learning Guide",
                "Data Structures Book",
                "AI Handbook",
                "Operating Systems",
                "Database Systems"
            ],

            "Clothing": [
                "Nike T-Shirt",
                "Adidas Hoodie",
                "Puma Shoes",
                "Jeans",
                "Casual Shirt",
                "Jacket"
            ],

            "Sports": [
                "Football",
                "Cricket Bat",
                "Basketball",
                "Tennis Racket",
                "Badminton Kit"
            ],

            "Furniture": [
                "Office Chair",
                "Study Table",
                "Wooden Desk",
                "Bookshelf",
                "Sofa Set",
                "Dining Table"
            ]
        }

        categories = list(products_by_category.keys())

        batch = []

        for i in range(200000):

            category = random.choice(categories)

            name = (
                random.choice(products_by_category[category])
                + " "
                + str(random.randint(1, 100000))
            )

            batch.append(
                Product(
                    name=name,
                    category=category,
                    price=Decimal(random.randint(100, 100000)),
                    created_at=timezone.now(),
                    updated_at=timezone.now()
                )
            )

            if len(batch) == 5000:
                Product.objects.bulk_create(batch)
                batch = []
                self.stdout.write(f"Inserted {i+1} products")

        if batch:
            Product.objects.bulk_create(batch)

        self.stdout.write(
            self.style.SUCCESS("200000 products created successfully")
        )