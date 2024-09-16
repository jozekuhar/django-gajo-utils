from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)


class Variant(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(
        "Product", related_name="variants", on_delete=models.CASCADE
    )
