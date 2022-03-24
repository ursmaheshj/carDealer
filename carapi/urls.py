from django.urls import path,include
from carapi import views

urlpatterns = [
    path('car', views.CarList.as_view()),
    path('car/<int:pk>',views.CarRetrieveUpdateDestroy.as_view()),
    path('car/expense/<int:pk>',views.ExpenseList.as_view()),
    path('car/sell/<int:pk>',views.SellList.as_view()),
]