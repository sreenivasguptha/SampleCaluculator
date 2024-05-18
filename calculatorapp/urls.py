from django.urls import path

from calculatorapp import views

urlpatterns = [
    path('',views.home),
    path('display',views.display)
]