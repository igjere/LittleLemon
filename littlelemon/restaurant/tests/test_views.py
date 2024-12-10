from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        
        # Create test menu items
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Pizza", Price=100, Inventory=50)
        Menu.objects.create(Title="Burger", Price=60, Inventory=45)
        
        # Set up the API client
        self.client = APIClient()
        
    def test_getall(self):
        # Authenticate the user
        self.client.force_authenticate(user=self.user)
        
        # Make GET request to the menu endpoint
        response = self.client.get('/api/menu-items/')
        
        # Get all menu items from database
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        
        # Check if the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the serialized data equals the response
        self.assertEqual(response.data, serializer.data) 