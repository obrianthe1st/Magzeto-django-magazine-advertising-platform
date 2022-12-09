import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register

from tests.factories import UserFactory

register(UserFactory)

@pytest.fixture()
def test_user(db):
    return User.objects.create(username='jack',email='jack@gmail.com')


@pytest.fixture()
def test_user2(db):
    return User.objects.create(username='jeff',email='jack@gmail.com',is_staff=False)