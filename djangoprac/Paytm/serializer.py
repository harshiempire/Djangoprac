from rest_framework import serializers
from django.core.validators import EmailValidator
from .models import User,Account
from django.contrib.auth.hashers import make_password
import random

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=30,
        validators=[
            EmailValidator(
                message="Enter a valid email address."
            )
        ]
    )
    
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password should be at least 6 characters long")
        return value
    
    def create(self,validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = super().create(validated_data)
        random_balance = round(random.uniform(1, 10000), 2)
        Account.objects.create(user=user, balance=random_balance)
        return user