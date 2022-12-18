from django.core.validators import RegexValidator

alphabetic_validator = RegexValidator(
    r"^[a-zA-Z ]*$", "Only alphabetic characters and spaces are allowed."
)

ruc_validator = RegexValidator(
    r"^(10|20|15|16|17)[0-9]{9}$",
    "Invalid RUC. It must start with 10, 20, 15, 16, or 17 and be 11 numbers long.",
)

numeric_validator = RegexValidator(r"^[0-9]*$", "Only numeric characters are allowed.")
