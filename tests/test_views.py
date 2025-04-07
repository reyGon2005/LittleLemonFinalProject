# test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pizza", price=10.99, inventory=15)

    def test_getall(self):
        response = self.client.get('/api/menu/')  # Ajusta esta URL si es diferente
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
