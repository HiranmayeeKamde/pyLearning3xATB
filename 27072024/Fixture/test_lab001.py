import pytest


@pytest.fixture()
def is_married():
    return True


def test_i_need_conf(is_married):
    assert is_married == True  # function use a variable when we mark as a fixture
