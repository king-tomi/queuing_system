# Create your views here.
# queuing_system/views.py

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import Customer, BankStaff, QueueEntry
from .serializers import CustomerSerializer, BankStaffSerializer, QueueEntrySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .utils import get_least_busy_staff, send_assignment_notification
from django.db.models import Count
    
# Customer ListAPIView and APIView
class CustomerListAPIView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


    def get(self, request):
        customers = self.get_queryset()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerAPIView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = CustomerSerializer

    def get_object(self, email, password):
        try:
            return Customer.objects.get(email=email, password=password)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'detail': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        customer = self.get_object(email, password)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'detail': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        customer = self.get_object(email, password)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'detail': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        customer = self.get_object(email, password)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# BankStaff ListAPIView and APIView
class BankStaffListAPIView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = BankStaffSerializer

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

class BankStaffAPIView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = BankStaffSerializer

    def get_object(self, email, password):
        try:
            return BankStaff.objects.get(email=email, password=password)
        except BankStaff.DoesNotExist:
            raise Http404

    def get(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'detail': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        bankstaff = self.get_object(email, password)
        serializer = BankStaffSerializer(bankstaff)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BankStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'detail': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        bankstaff = self.get_object(email, password)
        serializer = BankStaffSerializer(bankstaff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'detail': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        bankstaff = self.get_object(email, password)
        bankstaff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# QueueEntry ListAPIView and APIView
class QueueEntryListAPIView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner, IsAdminUser]
    serializer_class = QueueEntrySerializer

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

class QueueEntryAPIView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = QueueEntrySerializer

    def get_object(self, pk):
        try:
            return QueueEntry.objects.get(pk=pk)
        except QueueEntry.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queueentry = self.get_object(pk)
        serializer = QueueEntrySerializer(queueentry)
        return Response(serializer.data)

    def post(self, request):
        serializer = QueueEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    
class DashboardOverviewAPIView(GenericAPIView):
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

class StaffQueueLoadAPIView(GenericAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        staff_loads = QueueEntry.objects.values('staff__name').annotate(total=Count('id')).order_by('-total')
        return Response(staff_loads)