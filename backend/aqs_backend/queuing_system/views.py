# Create your views here.
# queuing_system/views.py

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, BankStaff, QueueEntry
from .serializers import CustomerSerializer, BankStaffSerializer, QueueEntrySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .utils import get_least_busy_staff, send_assignment_notification
from django.db.models import Count


# Customer ListAPIView and APIView
class CustomerListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# BankStaff ListAPIView and APIView
class BankStaffListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        bankstaff = BankStaff.objects.all()
        serializer = BankStaffSerializer(bankstaff, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BankStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankStaffAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            return BankStaff.objects.get(pk=pk)
        except BankStaff.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bankstaff = self.get_object(pk)
        serializer = BankStaffSerializer(bankstaff)
        return Response(serializer.data)

    def put(self, request, pk):
        bankstaff = self.get_object(pk)
        serializer = BankStaffSerializer(bankstaff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bankstaff = self.get_object(pk)
        bankstaff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# QueueEntry ListAPIView and APIView
class QueueEntryListAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner, IsAdminUser]

    def get(self, request):
        queueentries = QueueEntry.objects.all()
        serializer = QueueEntrySerializer(queueentries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QueueEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        queueentries = QueueEntry.objects.all()
        serializer = QueueEntrySerializer(queueentries, many=True)

        least_busy_staff = get_least_busy_staff()
        if least_busy_staff:
            queue_entry = serializer.save(staff=least_busy_staff)
            send_assignment_notification(least_busy_staff.email, queue_entry)
        else:
            queue_entry = serializer.save()

class QueueEntryAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            return QueueEntry.objects.get(pk=pk)
        except QueueEntry.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queueentry = self.get_object(pk)
        serializer = QueueEntrySerializer(queueentry)
        return Response(serializer.data)

    def put(self, request, pk):
        queueentry = self.get_object(pk)
        serializer = QueueEntrySerializer(queueentry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queueentry = self.get_object(pk)
        queueentry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DashboardOverviewAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_queues = QueueEntry.objects.count()
        active_queues = QueueEntry.objects.filter(status='Active').count()
        completed_queues = QueueEntry.objects.filter(status='Completed').count()
        staff_loads = QueueEntry.objects.values('staff').annotate(total=Count('id')).order_by('-total')
        
        data = {
            'total_queues': total_queues,
            'active_queues': active_queues,
            'completed_queues': completed_queues,
            'staff_loads': staff_loads,
        }
        return Response(data)

class StaffQueueLoadAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        staff_loads = QueueEntry.objects.values('staff__name').annotate(total=Count('id')).order_by('-total')
        return Response(staff_loads)