# queuing_system/serializers.py

from rest_framework import serializers
from .models import Customer, BankStaff, QueueEntry
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseUserSerializer

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

# BankStaff Serializer
class BankStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStaff
        fields = '__all__'

# QueueEntry Serializer
class QueueEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueEntry
        fields = '__all__'

class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'username', 'password']

class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'email', 'username', 'password']

