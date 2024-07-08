from django.db.models import Count
from django.core.mail import send_mail
from django.conf import settings
from .models import Customer, BankStaff, QueueEntry

def get_least_busy_staff():
    staff = BankStaff.objects.annotate(queue_count=Count('queueentry')).order_by('queue_count').first()
    return staff

def send_assignment_notification(staff_email, queue_entry):
    send_mail(
        'New Queue Assignment',
        f'You have been assigned a new queue entry: {queue_entry.customer_name} needs {queue_entry.service_needed}.',
        settings.DEFAULT_FROM_EMAIL,
        [staff_email],
        fail_silently=False,
    )