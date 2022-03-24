from rest_framework import generics,permissions
from rest_framework.parsers import JSONParser

from cardetails.models import Car, Expense, Sell
from .serializer import CarSerializer, ExpenseSerializer, SellSerializer
from carapi import serializer
from rest_framework.authtoken.models import Token 
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# @api_view(['POST'])
# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = request.data
#         user = authenticate(request,username=data['username'], password=data['password'])
#         if user is None:
#             return JsonResponse({'error':'Username or Password wrong'},status=401)
#         else:
#             try:
#                 token = Token.objects.get(user=user)
#             except:
#                 token = Token.objects.create(user=user)
#             return JsonResponse({'token':str(token)},status=200)

class CarList(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
         return Car.objects.filter(user=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class CarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Car.objects.filter(user=user)

class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        carmodel = Car.objects.get(pk=self.kwargs['pk'])
        return Expense.objects.filter(carmodel=carmodel)

    def perform_create(self, serializer):
        carmodel = Car.objects.get(pk=self.kwargs['pk'])
        serializer.save(carmodel=carmodel)

class SellList(generics.ListCreateAPIView):
    serializer_class = SellSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        carmodel = Car.objects.get(pk=self.kwargs['pk'])
        return Sell.objects.filter(carmodel=carmodel)

    def perform_create(self, serializer):
        carmodel = Car.objects.get(pk=self.kwargs['pk'])
        serializer.save(carmodel=carmodel)