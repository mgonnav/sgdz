from django.core.validators import MinValueValidator
from django.db import models

from sgz.utils.validators import alphabetic_validator, numeric_validator


class PaymentType(models.Model):
    """
    Physical model code: MF-05
    """

    name = models.CharField(
        max_length=50, unique=True, help_text="Name of the payment type."
    )

    def __str__(self):
        return self.name


class PointOfSale(models.Model):
    """
    Physical model code: MF-02
    """

    name = models.CharField(
        max_length=50, unique=True, help_text="Name of the point of sale."
    )

    def __str__(self):
        return self.name


class ShoeModel(models.Model):
    """
    Physical model code: MF-11
    """

    code = models.CharField(
        max_length=20, unique=True, help_text="Code of the shoe model."
    )
    name = models.CharField(max_length=50, help_text="Name of the shoe model.")
    brand = models.CharField(max_length=30, help_text="Brand of the shoe model.")
    color = models.CharField(max_length=20, help_text="Colour of the shoe model.")

    def __str__(self):
        return f"{self.code} | {self.name}"


class Product(models.Model):
    """
    Physical model code: MF-07
    """

    size = models.DecimalField(
        max_digits=8,
        decimal_places=1,
        validators=[MinValueValidator(0.0, "The size cannot be negative.")],
        help_text="Shoe size of the product.",
    )
    suggested_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.0, "The price cannot be negative.")],
        help_text="Suggested sale price for the product.",
    )
    shoe_model = models.ForeignKey(
        ShoeModel, on_delete=models.CASCADE, help_text="Shoe model for this product."
    )


class Provider(models.Model):
    """
    Physical model code: MF-13
    """

    ruc = models.CharField(
        max_length=11,
        validators=[numeric_validator],
        unique=True,
        help_text="RUC of the provider.",
    )
    company_name = models.CharField(max_length=30, help_text="Name of the provider.")
    contact_number = models.CharField(
        max_length=9,
        validators=[numeric_validator],
        help_text="Phone number of the provider's contact.",
    )
    contact_name = models.CharField(
        max_length=50,
        validators=[alphabetic_validator],
        help_text="Name of the provider's contact.",
    )

    def __str__(self):
        return f"{self.company_name} ({self.contact_name})"


class Storeroom(models.Model):
    """
    Physical model code: MF-09
    """

    name = models.CharField(
        max_length=50, unique=True, help_text="Name of the storeroom."
    )
    allocations = models.ManyToManyField(
        Product,
        related_name="allocations",
        through="Allocation",
        help_text="Products allocated in a specific storeroom.",
    )

    def __str__(self):
        return self.name


class Allocation(models.Model):
    """
    Physical model code: MF-08
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    storeroom = models.ForeignKey(Storeroom, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
