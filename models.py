from django.core.validators import RegexValidator
from django.db import models


class Student(models.Model):
    """
    Represents a student record.
    SOP Section 7.3 Database Design: primary key, appropriate data types,
    NOT NULL / UNIQUE constraints where required.
    """

    YEAR_CHOICES = [
        (1, 'Year 1'),
        (2, 'Year 2'),
        (3, 'Year 3'),
        (4, 'Year 4'),
        (5, 'Year 5'),
    ]

    phone_validator = RegexValidator(
        regex=r'^\d{10}$',
        message='Phone number must be exactly 10 digits.'
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES)
    phone = models.CharField(
        max_length=10, blank=True, null=True, validators=[phone_validator]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.roll_number})'
