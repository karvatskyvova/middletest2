from django.test import TestCase
from recipe.models import Category, Recipe

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Dessert')

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), 'Dessert')

