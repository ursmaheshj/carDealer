from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    # Car_detail
    fuelList = (('Petrol','Petrol'),('Diesel','Diesel'),('Petrol-CNG','Petrol-CNG'))
    ownerChangeList = (('First','First'),('Second','Second'),('Third','Third'),('Fourth','Fourth'),('Fifth','Fifth'))
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    vehicle_no = models.CharField(max_length=10)
    detail = models.TextField(blank=True)
    vehicleDate = models.DateField()
    fuelType = models.CharField(max_length=15,choices=fuelList)
    ownerChange = models.CharField(max_length=15,choices=ownerChangeList)

    # Owners_detail
    OwnerName = models.CharField(max_length=100)
    aadharNo = models.IntegerField()
    ownerAddress = models.TextField()

    # Seller_detail
    sellerName = models.CharField(max_length=100)
    sellerAddress = models.TextField()
    mobileNo = models.IntegerField()

    # Purchase_detail
    purchaseDate = models.DateField()
    purchaseAmt = models.FloatField(max_length=7)
    advanceGiven = models.FloatField(max_length=7)
    balanceRemaining = models.FloatField(max_length=7,blank=True)
    agentExcuse = models.FloatField(max_length=7)
    def save(self, *args, **kwargs):
        self.balanceRemaining = self.purchaseAmt - self.advanceGiven
        return super().save()

class Expense(models.Model):
    carmodel = models.OneToOneField(Car,on_delete=models.CASCADE,primary_key=True)
    travelling = models.FloatField(max_length=7)
    meterWork = models.FloatField(max_length=7)
    repairingWork = models.FloatField(max_length=7)
    dentingAndPainting = models.FloatField(max_length=7)
    accessoryWork = models.FloatField(max_length=7)
    rubbingPolish = models.FloatField(max_length=7)
    total = models.FloatField(max_length=7,blank=True)

    def save(self, *args, **kwargs):
        self.total = self.travelling + self.meterWork + self.repairingWork + self.dentingAndPainting + self.accessoryWork + self.rubbingPolish
        return super().save()

class Sell(models.Model):
    carmodel = models.OneToOneField(Car,on_delete=models.CASCADE,primary_key=True)
    buyerName = models.CharField(max_length=100)
    buyerAddress = models.TextField()
    mobile = models.IntegerField()
    aadhar = models.IntegerField()

    # expectedAmt = models.FloatField(max_length=7)
    dealDate = models.DateField()
    dealAmt = models.FloatField(max_length=7)
    advanceAmt = models.FloatField(max_length=7)
    balanceAmt = models.FloatField(max_length=7,blank=True)
    documentCharges = models.FloatField(max_length=7)
    def save(self, *args, **kwargs):
        self.balanceAmt = self.dealAmt - self.advanceAmt
        return super().save()


    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # important = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.buyerName
