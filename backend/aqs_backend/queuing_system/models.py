from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default='')
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BankStaff(models.Model):
    full_name = models.CharField(max_length=150)
    staff_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, default='')
    position = models.CharField(max_length=100)
    password = models.CharField(max_length=128, unique=True, default='')  # Length suitable for hashed passwords

    def save(self, *args, **kwargs):
        # Hash the password if it's being created or updated
        if not self.pk:  # New instance
            self.password = make_password(self.password)
        else:  # Updating existing instance
            old_password = BankStaff.objects.get(pk=self.pk).password
            if not check_password(self.password, old_password):
                self.password = make_password(self.password)
        super(BankStaff, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class TransactionType(models.Model):
    TRANSACTION_CHOICES = [
        ('TELLER', 'Teller Transactions'),
        ('CSO', 'CSO Transactions'),
    ]

    type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES, unique=True)

    def __str__(self):
        return self.type

class QueueEntry(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bank_staff = models.ForeignKey(BankStaff, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return f"{self.customer} - {self.bank_staff} - {self.transaction_type}"