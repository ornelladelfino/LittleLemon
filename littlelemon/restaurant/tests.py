from django.test import TestCase
from .models import Menu
from .views import MenuView
from django.urls import reverse
from .serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status, response
from django.contrib.auth.models import User
import json

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, menu_item_description="dessert")
        self.assertEqual(item.name, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.menu_item_description, "dessert")
        


