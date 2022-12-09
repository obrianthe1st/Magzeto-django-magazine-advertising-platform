import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_check_password(test_user):
    test_user.set_password("jacky")
    assert test_user.check_password("jacky") is True

#we have to use the pytest.mark.django_db decorator to save data in our test db 
@pytest.mark.django_db
def test_check_username(user_factory):
    user = user_factory.create()
    print(user_factory.username)
    print("hello")
    assert True



