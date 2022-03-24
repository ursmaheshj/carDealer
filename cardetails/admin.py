from django.contrib import admin
from .models import Car,Sell,Expense

# Register your models here.
admin.site.register(Car)
admin.site.register(Expense)
admin.site.register(Sell)