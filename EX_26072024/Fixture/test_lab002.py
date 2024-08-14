import pytest


@pytest.fixture()
def sample_data1():
    data = [1, 2, 3, 4, 5]  # type - List
    return data


@pytest.fixture()
def sample_data2():
    return True


def test_i_consume_sample_1_2(sample_data1, sample_data2):
    print(sample_data1)  # function use a variable when we mark as a fixture
    print(sample_data2)
