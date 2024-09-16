import random
from tests_app.dummy.models import Product, Variant


def create_product():
    return Product.objects.create(name=f"Product #{random.randint(1000, 9999)}")


def create_variant(product):
    return Variant.objects.create(
        name=f"Variant #{random.randint(1000, 9999)}", product=product
    )


def create_product_with_variants(num_of_variants):
    product = create_product()

    for _ in range(num_of_variants):
        create_variant(product)

    return product
