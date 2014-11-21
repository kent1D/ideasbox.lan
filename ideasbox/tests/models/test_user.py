import pytest

from django.contrib.auth import get_user_model

from .. import UserFactory

pytestmark = pytest.mark.django_db


def test_it_should_create_a_default_user_from_factory():
    user = UserFactory()
    assert user.pk is not None


def test_it_should_override_fields_passed_to_factory():
    user = UserFactory()
    assert user.short_name == "Sankara"
    another = UserFactory(short_name="Che")
    assert another.short_name == "Che"


def test_get_short_name_should_return_short_name():
    user = UserFactory()
    assert user.get_short_name() == "Sankara"


def test_get_full_name_should_return_full_name():
    user = UserFactory()
    assert user.get_full_name() == "Thomas Sankara"


def test_create_user():
    model = get_user_model()
    user = model.objects.create_user('123456')
    assert user.pk is not None
    assert user.serial == '123456'


def test_create_superuser():
    model = get_user_model()
    user = model.objects.create_superuser('123456', 'passw0rd')
    assert user.pk is not None
    assert user.serial == '123456'
    assert user.is_admin


def test_client_login(client, user):
    assert client.login(serial=user.serial, password='password')
