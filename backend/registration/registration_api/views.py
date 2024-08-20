#from django.shortcuts import render
from rest_framework import generics
from .models import Registration
from .serializers import RegistrationSerializer

class RegistrationCreateView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

# Create your views here.
