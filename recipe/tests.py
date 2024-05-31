from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Dessert')

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), 'Dessert')

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Dessert')
        self.recipe = Recipe.objects.create(
            title='Chocolate Cake',
            description='A delicious chocolate cake',
            instructions='Mix ingredients and bake',
            ingredients='Flour, sugar, cocoa, baking powder, eggs, milk, oil, vanilla extract',
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertTrue(isinstance(self.recipe, Recipe))
        self.assertEqual(self.recipe.__str__(), 'Chocolate Cake')
        self.assertEqual(self.recipe.category.name, 'Dessert')
