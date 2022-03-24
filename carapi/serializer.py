from pyexpat import model
from rest_framework import serializers
from cardetails.models import Car,Expense,Sell

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        read_only_fields = ['id','user','balanceRemaining']
        fields = ['id','model','color','vehicle_no','detail','vehicleDate','fuelType','ownerChange','OwnerName','ownerAddress','aadharNo',
        'sellerName','sellerAddress','mobileNo','purchaseDate','purchaseAmt','advanceGiven','balanceRemaining','agentExcuse']

class ExpenseSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    class Meta:
        model = Expense
        fields = ['travelling','meterWork','repairingWork','dentingAndPainting','accessoryWork','rubbingPolish','total']
        
class SellSerializer(serializers.ModelSerializer):
    balanceAmt = serializers.ReadOnlyField()
    class Meta:
        model = Sell
        fields = ['buyerName','buyerAddress','mobile','aadhar','dealDate','dealAmt','advanceAmt','balanceAmt','documentCharges']
    
   