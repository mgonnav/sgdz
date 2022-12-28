# Generated by Django 4.0.8 on 2022-12-28 23:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Allocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "stock",
                    models.PositiveIntegerField(
                        help_text="Stock of the product in the storeroom."
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the brand.", max_length=30, unique=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the color.", max_length=20, unique=True
                    ),
                ),
                (
                    "hex_code",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Hexadecimal code of the color.",
                        max_length=7,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PaymentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the payment type.",
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PointOfSale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the point of sale.",
                        max_length=50,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "size",
                    models.DecimalField(
                        decimal_places=1,
                        help_text="Shoe size of the product.",
                        max_digits=8,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0.0, "The size cannot be negative."
                            )
                        ],
                    ),
                ),
                (
                    "suggested_price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Suggested sale price for the product.",
                        max_digits=8,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0.0, "The price cannot be negative."
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ruc",
                    models.CharField(
                        help_text="RUC of the provider.",
                        max_length=11,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^(10|20|15|16|17)[0-9]{9}$",
                                "Invalid RUC. It must start with 10, 20, 15, 16, or 17 and be 11 numbers long.",
                            )
                        ],
                    ),
                ),
                (
                    "company_name",
                    models.CharField(help_text="Name of the provider.", max_length=30),
                ),
                (
                    "contact_name",
                    models.CharField(
                        help_text="Name of the provider's contact.",
                        max_length=50,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z ]*$",
                                "Only alphabetic characters and spaces are allowed.",
                            )
                        ],
                    ),
                ),
                (
                    "contact_number",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Phone number of the provider's contact.",
                        max_length=9,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9]*$", "Only numeric characters are allowed."
                            ),
                            django.core.validators.MinLengthValidator(9),
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Storeroom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the storeroom.", max_length=50, unique=True
                    ),
                ),
                (
                    "allocations",
                    models.ManyToManyField(
                        help_text="Products allocated in a specific storeroom.",
                        related_name="storerooms",
                        through="management.Allocation",
                        to="management.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShoeModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        help_text="Code of the shoe model.", max_length=20, unique=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the shoe model.", max_length=50
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        help_text="Brand of the shoe model.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.brand",
                    ),
                ),
                (
                    "colors",
                    models.ManyToManyField(
                        help_text="Colour of the shoe model.",
                        related_name="shoe_models",
                        to="management.color",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="shoe_model",
            field=models.ForeignKey(
                help_text="Shoe model for this product.",
                on_delete=django.db.models.deletion.CASCADE,
                to="management.shoemodel",
            ),
        ),
        migrations.AddField(
            model_name="allocation",
            name="product",
            field=models.ForeignKey(
                help_text="Product allocated in a specific storeroom.",
                on_delete=django.db.models.deletion.CASCADE,
                to="management.product",
            ),
        ),
        migrations.AddField(
            model_name="allocation",
            name="storeroom",
            field=models.ForeignKey(
                help_text="Storeroom where the product is allocated.",
                on_delete=django.db.models.deletion.CASCADE,
                to="management.storeroom",
            ),
        ),
    ]
