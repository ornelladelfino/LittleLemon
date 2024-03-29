from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'index.html', {})


class MenuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated]
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   