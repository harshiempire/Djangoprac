from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):
    username = models.CharField(
        max_length=30,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
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

    def clean(self):
        if not self.username.isalnum():
            raise ValidationError('Username should only contain alphanumeric characters')
        if len(self.password) < 6:
            raise ValidationError('Password should be at least 6 characters long')

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return f"Account of {self.user.username} with balance {self.balance}"
