from django.db import models

from sgz.utils.validators import alphabetic_validator, numeric_validator


class Provider(models.Model):
    """
    Relational model code: MR-03
    """

    ruc = models.CharField(
        max_length=11,
        validators=[numeric_validator],
        unique=True,
        help_text="Provider RUC.",
    )
    company_name = models.CharField(max_length=30, help_text="Provider name.")
    contact_number = models.CharField(
        max_length=9,
        validators=[numeric_validator],
        help_text="Provider phone number.",
    )
    contact_name = models.CharField(
        max_length=50,
        validators=[alphabetic_validator],
        help_text="Provider contact name.",
    )

    def __str__(self):
        return f"{self.company_name} ({self.contact_name})"


class PointOfSale(models.Model):
    """
    Relational model code: MR-02
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Provider contact name.",
    )

    def __str__(self):
        return self.name
