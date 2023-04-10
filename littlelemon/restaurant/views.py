from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core import serializers
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from datetime import datetime

from .serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu
from django.views.decorators.csrf import csrf_exempt

# 
# API views
#
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

#class BookingViewSet(generics.ListCreateAPIView):
#    permission_classes = [IsAuthenticated]
#    queryset = Booking.objects.all()
#    serializer_class = BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})

def about(request):
    return render(request, './about.html')

def reservations(request:HttpRequest) -> HttpResponse:
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'reservations.html',{"bookings":booking_json})