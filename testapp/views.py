from django.shortcuts import render

# Create your views here
from rest_framework.generics import  ListAPIView,ListCreateAPIView,RetrieveAPIView,CreateAPIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.generics import  ListAPIView
from testapp.pagination import Mypagination1, Mypagination2,Mypagination3
from testapp.serializers import EmployeeSerializer



class EmployeeAPI(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = Mypagination1
    # def get_queryset(self):
    #     qs = Employee.objects.all()
    #     ename = self.request.GET.get('ename')
    #     if ename is not None:
    #         qs = qs.filter(ename__icontains= 's')
    #     return qs
    search_fields= ('=eno',)
    ordering_fields = ('eno',)