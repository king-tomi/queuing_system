from django.contrib import admin
from .models import Customer, BankStaff, QueueEntry

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')

@admin.register(BankStaff)
class BankStaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'staff_id', 'position')
    search_fields = ('full_name', 'staff_id', 'position')

@admin.register(QueueEntry)
class QueueEntryAdmin(admin.ModelAdmin):
    list_display = ('customer', 'bank_staff', 'timestamp', 'is_completed', 'description')
    list_filter = ('bank_staff', 'is_completed')
    search_fields = ('customer__first_name', 'customer__last_name', 'bank_staff__full_name')