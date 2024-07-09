# queuing_system/serializers.py

from rest_framework import serializers
from .models import Customer, BankStaff, QueueEntry
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number']

# BankStaff Serializer
class BankStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStaff
        fields = ['full_name', 'staff_id', 'email', 'phone_number']

# QueueEntry Serializer
class QueueEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueEntry
        fields = ['is_completed', 'description']

class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'username', 'password']

class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'email', 'username', 'password']

