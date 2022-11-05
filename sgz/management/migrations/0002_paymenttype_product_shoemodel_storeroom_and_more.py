# Generated by Django 4.0.8 on 2022-11-05 05:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
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
                        help_text="Name of the shoe model.", max_length=50, unique=True
                    ),
                ),
                (
                    "brand",
                    models.CharField(
                        help_text="Brand of the shoe model.", max_length=30, unique=True
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        help_text="Colour of the shoe model.",
                        max_length=20,
                        unique=True,
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
            ],
        ),
        migrations.AlterField(
            model_name="pointofsale",
            name="name",
            field=models.CharField(
                help_text="Name of the point of sale.", max_length=50, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="company_name",
            field=models.CharField(help_text="Name of the provider.", max_length=30),
        ),
        migrations.AlterField(
            model_name="provider",
            name="contact_name",
            field=models.CharField(
                help_text="Name of the provider's contact.",
                max_length=50,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[a-zA-Z]*$", "Only alphabetic characters are allowed."
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="contact_number",
            field=models.CharField(
                help_text="Phone number of the provider's contact.",
                max_length=9,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9]*$", "Only numeric characters are allowed."
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="ruc",
            field=models.CharField(
                help_text="RUC of the provider.",
                max_length=11,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9]*$", "Only numeric characters are allowed."
                    )
                ],
            ),
        ),
    ]
