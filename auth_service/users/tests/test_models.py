from pprint import pprint

from django.test import TestCase
from faker import Faker

from ..models import User


class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        faker = Faker()
        cls.faker = faker
        cls.user_data = {
            "email": faker.email(),
            "password": faker.password()
        }

    def test_create_customer(self):
        customer = User.objects.create_customer(**self.user_data)
        pprint(customer.serializer(), indent=4)
        self.assertTrue(customer.is_customer)
