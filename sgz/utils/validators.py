from django.core.validators import RegexValidator

alphanumeric_validator = RegexValidator(
    r"^[0-9a-zA-Z ]*$", "Only alphanumeric characters are allowed."
)

alphabetic_validator = RegexValidator(
    r"^[a-zA-Z ]*$", "Only alphabetic characters are allowed."
)

numeric_validator = RegexValidator(r"^[0-9]*$", "Only numeric characters are allowed.")
