from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="weow", price=12.11, inventory=1)
        self.assertEqual(str(item), "weow : 12.11")
