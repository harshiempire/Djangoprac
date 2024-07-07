from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    email_validator = EmailValidator(
        message="Enter a valid email address."
    )
    
    username = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        validators=[email_validator],
        help_text="Required. 30 characters or fewer. Must be a valid email address.",
    )
    password = models.CharField(
        max_length=128,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk:  # Only hash the password for new users
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def clean(self):
        if len(self.password) < 6:
            raise ValidationError('Password should be at least 6 characters long')

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return f"Account of {self.user.username} with balance {self.balance}"