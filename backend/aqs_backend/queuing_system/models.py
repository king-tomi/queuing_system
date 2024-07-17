from django.db import models

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

    def __str__(self):
        return self.full_name
    
class QueueEntry(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bank_staff = models.ForeignKey(BankStaff, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return f"{self.customer} - {self.bank_staff}"