# queuing_system/urls.py

from django.urls import path
from .views import (
    CustomerListAPIView, CustomerAPIView,
    BankStaffListAPIView, BankStaffAPIView,
    QueueEntryListAPIView, QueueEntryAPIView,
    DashboardOverviewAPIView, StaffQueueLoadAPIView
)

urlpatterns = [
    # Customers URLs
    path('customers/', CustomerListAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerAPIView.as_view(), name='customer-detail'),

    # BankStaff URLs
    path('bankstaff/', BankStaffListAPIView.as_view(), name='bankstaff-list'),
    path('bankstaff/<int:pk>/', BankStaffAPIView.as_view(), name='bankstaff-detail'),

    # QueueEntry URLs
    path('queues/', QueueEntryListAPIView.as_view(), name='queueentry-list'),
    path('queues/<int:pk>/', QueueEntryAPIView.as_view(), name='queueentry-detail'),

    #admin urls
    path('admin/dashboard/overview/', DashboardOverviewAPIView.as_view(), name='dashboard-overview'),
    path('admin/queues/', QueueEntryListAPIView.as_view(), name='queue-list'),
    path('admin/staff-load/', StaffQueueLoadAPIView.as_view(), name='staff-queue-load'),
]