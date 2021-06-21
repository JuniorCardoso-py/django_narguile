from django.test import TestCase
from .models import Narguile

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        narguile = Narguile.objects.create(
            name='TestName', price=250.00, heitgt_type='Tall', stock=12)
        narguile.save()
        self.response_get = self.client.get('/narguile/')

    def test_route_list_all_returning_status_code_200(self):

        self.assertEqual(self.response_get.status_code, 200)

    def test_route_list_all_returning_an_valid_template(self):

        self.assertTemplateUsed(
            self.response_get, 'narguile.html')

    def test_route_list_all_returning_an_expected_response(self):

        self.assertEqual(
            self.response_get.context['narguile'][0].name, "TestName")
            
        self.assertEqual(
            self.response_get.context['narguile'][0].price, 250.00)

        self.assertEqual(self.response_get.context['narguile'][0].stock, 12)
        self.assertEqual(self.response_get.context['narguile'][0].heitgt_type, "Tall")

class TestModels(TestCase):

    def test_instance_of_class_Narguile(self):

        narguile = Narguile.objects.create(
            name='TestName', price=250.00, heitgt_type='Tall', stock=12)

        
        self.assertIsInstance(narguile, Narguile)

    def test_attributes_are_correctly_created(self):

        narguile = Narguile.objects.create(
            name='TestName', price=250.00, heitgt_type='Tall', stock=12)

        
        self.assertEqual(narguile.name, "TestName")
        self.assertEqual(narguile.price, 250)
        self.assertEqual(narguile.heitgt_type, "Tall")
        self.assertEqual(narguile.stock, 12)
    
