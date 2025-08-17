import os
import django
from decimal import Decimal
import random

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_backend_graphql_crm.settings")
django.setup()

from crm.models import Customer, Product, Order


def seed():
    # Clear old data
    Order.objects.all().delete()
    Product.objects.all().delete()
    Customer.objects.all().delete()

    # Create customers
    customers = [
        Customer(name="Alice Johnson", email="alice@example.com", phone="+1234567890"),
        Customer(name="Bob Smith", email="bob@example.com", phone="+1987654321"),
        Customer(name="Charlie Brown", email="charlie@example.com", phone="555-555-5555"),
    ]
    Customer.objects.bulk_create(customers)

    # Create products
    products = [
        Product(name="Laptop", price=Decimal("1200.50"), stock=10),
        Product(name="Smartphone", price=Decimal("800.00"), stock=25),
        Product(name="Headphones", price=Decimal("150.75"), stock=50),
    ]
    Product.objects.bulk_create(products)

    # Fetch saved objects
    customers = list(Customer.objects.all())
    products = list(Product.objects.all())

    # Create orders
    for i in range(5):
        customer = random.choice(customers)
        chosen_products = random.sample(products, k=random.randint(1, len(products)))
        total_amount = sum([p.price for p in chosen_products])
        order = Order.objects.create(customer=customer, total_amount=total_amount)
        order.products.set(chosen_products)

    print("✅ Database seeded successfully with customers, products, and orders!")


if __name__ == "__main__":
    seed()
