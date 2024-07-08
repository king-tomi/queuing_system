from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create sample users for frontend testing'

    def handle(self, *args, **kwargs):
        # Create a list of sample users
        sample_users = [
            {'username': 'admin', 'email': 'admin@example.com', 'password': 'adminpass', 'is_staff': True, 'is_superuser': True},
            {'username': 'staff1', 'email': 'staff1@example.com', 'password': 'staffpass', 'is_staff': True},
            {'username': 'staff2', 'email': 'staff2@example.com', 'password': 'staffpass', 'is_staff': True},
            {'username': 'customer1', 'email': 'customer1@example.com', 'password': 'customerpass'},
            {'username': 'customer2', 'email': 'customer2@example.com', 'password': 'customerpass'},
        ]

        for user_data in sample_users:
            if not User.objects.filter(username=user_data['username']).exists():
                User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password'],
                    is_staff=user_data.get('is_staff', False),
                    is_superuser=user_data.get('is_superuser', False)
                )
                self.stdout.write(self.style.SUCCESS(f"Created user {user_data['username']}"))

        self.stdout.write(self.style.SUCCESS('Sample users created successfully'))