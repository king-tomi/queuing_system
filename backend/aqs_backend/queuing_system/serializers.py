# queuing_system/serializers.py
from rest_framework import serializers
from .models import Customer, BankStaff, QueueEntry, TransactionType
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer
from django.contrib.auth.hashers import make_password, check_password

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number']

# BankStaff Serializer
class BankStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStaff
        fields = ['id', 'full_name', 'position', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is write-only
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

# TransactionType Serializer
class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ['type']

# QueueEntry Serializer
class QueueEntrySerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    bank_staff = BankStaffSerializer()
    transaction_type = TransactionTypeSerializer()

    class Meta:
        model = QueueEntry
        fields = ['customer', 'bank_staff', 'transaction_type', 'timestamp', 'is_completed', 'description']

# UserCreate Serializer
class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'username', 'password']

# CurrentUser Serializer
class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'email', 'username', 'password']