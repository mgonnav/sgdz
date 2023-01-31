# Generated by Django 4.0.8 on 2023-01-30 18:11

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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
                    ),
                ),
                (
                    "stock",
                    models.PositiveIntegerField(
                        help_text="Stock of the product in the storeroom."
                    ),
                ),
                (
                    "foot",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Pie izquierdo"),
                            (1, "Pie derecho"),
                            (2, "Ambos pies"),
                        ],
                        default=2,
                        help_text="Foot of the product.",
                    ),
                ),
                (
                    "exhibition",
                    models.BooleanField(
                        default=False,
                        help_text="Whether the product is on exhibition or not.",
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the brand.", max_length=30, unique=True
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the color.", max_length=30, unique=True
                    ),
                ),
                (
                    "hex_code",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Hexadecimal code of the color.",
                        max_length=7,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^#(?:[0-9a-fA-F]{3}){1,2}$",
                                "Código de color inválido. Por favor use un código hexadecimal en formato de 6 dígitos.",
                            )
                        ],
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
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
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
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
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
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
                                "RUC inválido. Debe estar conformado por números y empezar por 10, 20, 15, 16 o 17.",
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
                                "^[a-zA-Z ]*$", "Solo se permiten letras y espacios."
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
                                "^[0-9]*$", "Solo se permiten números."
                            ),
                            django.core.validators.MinLengthValidator(9),
                        ],
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
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
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
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
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified at",
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
                (
                    "storeroom",
                    models.OneToOneField(
                        help_text="Storeroom associated with the point of sale.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="point_of_sale",
                        to="management.storeroom",
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
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
